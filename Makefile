SHELL := /bin/sh
MAIN := main.tex
BUILD := build
OUTPUT := 因果推理深度读本.pdf
CONTENT := chapters/*.tex
TEX_SOURCES := main.tex bookstyle.tex $(CONTENT)
AUDIT_SOURCES := $(TEX_SOURCES) references.bib README.md

.PHONY: pdf check watch clean

pdf:
	mkdir -p $(BUILD) $(dir $(OUTPUT))
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(BUILD) $(MAIN)
	cp $(BUILD)/main.pdf $(OUTPUT)

check: pdf
	@test -s $(OUTPUT)
	@! grep -E "Undefined control sequence|Citation '.+' undefined|Reference '.+' undefined|There were undefined references|multiply defined|Missing character|Please \(re\)run Biber|Empty bibliography|Overfull" $(BUILD)/main.log
	@han_count=$$(perl -CSDA -ne '$$n += () = /\p{Han}/g; END {print "$$n\n"}' chapters/*.tex); \
		test "$$han_count" -ge 120000 -a "$$han_count" -le 135000; \
		printf '全书汉字数：%s（验收范围：120000--135000）\n' "$$han_count"
	@core_han=$$(perl -CSDA -ne '$$n += () = /\p{Han}/g; END {print "$$n\n"}' chapters/chapter-*.tex); \
		test "$$core_han" -ge 90000 -a "$$core_han" -le 110000; \
		printf '主线正文汉字数：%s（验收范围：90000--110000）\n' "$$core_han"
	@chapter_count=$$(find chapters -maxdepth 1 -type f -name 'chapter-*.tex' | wc -l | tr -d ' '); \
		appendix_count=$$(find chapters -maxdepth 1 -type f -name 'appendix-*.tex' | wc -l | tr -d ' '); \
		section_count=$$(perl -ne '$$c++ while /^\\section\{/g; END {print "$$c\n"}' chapters/chapter-*.tex); \
		subsection_count=$$(perl -ne '$$c++ while /^\\subsection\{/g; END {print "$$c\n"}' chapters/chapter-*.tex); \
		test "$$chapter_count" -eq 11 -a "$$appendix_count" -eq 4; \
		test "$$section_count" -ge 30 -a "$$section_count" -le 40; \
		test "$$subsection_count" -ge 90 -a "$$subsection_count" -le 115; \
		printf '结构验收：%s章、%s附录、%s个一级节、%s个二级节。\n' "$$chapter_count" "$$appendix_count" "$$section_count" "$$subsection_count"
	@for file in chapters/chapter-*.tex; do \
		chapter_han=$$(perl -CSDA -ne '$$n += () = /\p{Han}/g; END {print "$$n\n"}' "$$file"); \
		test "$$chapter_han" -ge 6500 || { printf '章节篇幅不足：%s（%s汉字）\n' "$$file" "$$chapter_han"; exit 1; }; \
	done
	@for file in chapters/chapter-*.tex; do \
		perl -CSDA -0777 -e '$$s=<>; @p=split(/(?=^\\section\{)/m,$$s); shift @p; for $$p (@p){$$n=()=$$p=~/\p{Han}/g; exit 1 if $$n<1200}' "$$file" \
			|| { printf '一级节篇幅不足：%s\n' "$$file"; exit 1; }; \
		perl -CSDA -0777 -e '$$s=<>; @p=split(/(?=^\\(?:section|subsection)\{)/m,$$s); for $$p (@p){next unless $$p=~/^\\subsection\{/; $$n=()=$$p=~/\p{Han}/g; exit 1 if $$n<500}' "$$file" \
			|| { printf '二级节篇幅不足：%s\n' "$$file"; exit 1; }; \
	done
	@perl -ne 'exit 1 if /[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/' $(AUDIT_SOURCES)
	@perl -CSDA -ne 'exit 1 if /[\x{2010}\x{2011}\x{2012}\x{2013}\x{2014}\x{2015}]/' $(AUDIT_SOURCES)
	@perl -ne 'exit 1 if /=sum_|TODO|TBD|FIXME|待补|待写|占位/' $(AUDIT_SOURCES)
	@perl -ne 'while(/\\(?:textcite|parencite)(?:\[[^]]*\])?\{([^}]+)\}/g){print join("\n",split(/,/,$$1)),"\n"}' chapters/*.tex | sort -u > $(BUILD)/cited-keys.txt
	@perl -ne 'print "$$1\n" if /^@[[:alpha:]]+\{([^,]+)/' references.bib | sort -u > $(BUILD)/bib-keys.txt
	@cited_count=$$(wc -l < $(BUILD)/cited-keys.txt | tr -d ' '); \
		test "$$cited_count" -ge 210 || { printf '全书独立来源不足：%s（最低210）\n' "$$cited_count"; exit 1; }
	@for file in chapters/chapter-*.tex; do \
		chapter_keys=$$(perl -ne 'while(/\\(?:textcite|parencite)(?:\[[^]]*\])?\{([^}]+)\}/g){print join("\n",split(/,/,$$1)),"\n"}' "$$file" | sort -u | wc -l | tr -d ' '); \
		test "$$chapter_keys" -ge 17 || { printf '章节独立来源不足：%s（%s，最低17）\n' "$$file" "$$chapter_keys"; exit 1; }; \
	done
	@comm -23 $(BUILD)/cited-keys.txt $(BUILD)/bib-keys.txt > $(BUILD)/missing-bib-keys.txt
	@comm -13 $(BUILD)/cited-keys.txt $(BUILD)/bib-keys.txt > $(BUILD)/uncited-bib-keys.txt
	@test ! -s $(BUILD)/missing-bib-keys.txt || { printf '正文引用缺失书目条目：\n'; cat $(BUILD)/missing-bib-keys.txt; exit 1; }
	@test ! -s $(BUILD)/uncited-bib-keys.txt || { printf '书目存在未被引用条目：\n'; cat $(BUILD)/uncited-bib-keys.txt; exit 1; }
	@cd $(BUILD) && biber --tool --nolog --validate-datamodel --output-file validated-references.bib ../references.bib > bibliography-validation.log 2>&1
	@! grep -E 'WARN|ERROR' $(BUILD)/bibliography-validation.log
	@printf '引文闭合：%s/%s；书目数据模型与 PDF 日志检查通过。\n' "$$(wc -l < $(BUILD)/cited-keys.txt | tr -d ' ')" "$$(wc -l < $(BUILD)/bib-keys.txt | tr -d ' ')"
	@perl -ne 'while(/\\label\{([^}]+)\}/g){print "$$1\n"}' $(TEX_SOURCES) | sort > $(BUILD)/defined-labels.txt
	@uniq -d $(BUILD)/defined-labels.txt > $(BUILD)/duplicate-labels.txt
	@test ! -s $(BUILD)/duplicate-labels.txt || { printf '重复label：\n'; cat $(BUILD)/duplicate-labels.txt; exit 1; }
	@perl -ne 'while(/\\(?:ref|cref|pageref|eqref|autoref)\{([^}]+)\}/g){print join("\n",split(/,/,$$1)),"\n"}' $(TEX_SOURCES) | sort -u > $(BUILD)/used-labels.txt
	@comm -23 $(BUILD)/used-labels.txt $(BUILD)/defined-labels.txt > $(BUILD)/undefined-labels.txt
	@test ! -s $(BUILD)/undefined-labels.txt || { printf '引用了未定义的label：\n'; cat $(BUILD)/undefined-labels.txt; exit 1; }
	@printf '交叉引用闭合：%s个label全部唯一且被解析。\n' "$$(uniq $(BUILD)/defined-labels.txt | wc -l | tr -d ' ')"
	@perl -CSDA -ne 'while(/\\(?:term|index)\{([^}]*)\}/g){$$e=$$1; print "$$ARGV:行$$.: $$e\n" if $$e=~/[\x24#%^_~{}]|\\\\/}' $(CONTENT) > $(BUILD)/bad-index-entries.txt
	@test ! -s $(BUILD)/bad-index-entries.txt || { printf '索引条目含未转义特殊字符：\n'; cat $(BUILD)/bad-index-entries.txt; exit 1; }
	@perl -CSDA -ne 'while(/\\(?:term|index)\{([^}]*)\}/g){$$r=$$1; $$k=$$r; $$k=~s/\s+//g; $$k=~s/（/(/g; $$k=~s/）/)/g; print "$$k\t$$r\n"}' $(CONTENT) | sort > $(BUILD)/index-entries.txt
	@awk -F'\t' '{if(!($$1 in seen)){seen[$$1]=$$2}else if(seen[$$1]!=$$2){print $$0}}' $(BUILD)/index-entries.txt > $(BUILD)/index-collisions.txt
	@test ! -s $(BUILD)/index-collisions.txt || { printf '同一术语存在多种索引写法：\n'; cat $(BUILD)/index-collisions.txt; exit 1; }
	@printf '索引一致性：%s个索引条目无写法冲突。\n' "$$(cut -f2 $(BUILD)/index-entries.txt | sort -u | wc -l | tr -d ' ')"

watch:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(BUILD) -pvc $(MAIN)

clean:
	rm -rf $(BUILD) tmp
	rm -f references.bib.blg
	find . -type f -name .DS_Store -delete
