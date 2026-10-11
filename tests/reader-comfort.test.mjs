import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {READER_DEFAULTS, READER_THEMES, normalizeReaderPreferences, isCurrentBookPath} from '../assets/reader-comfort.mjs';
const root = new URL('../', import.meta.url);
const read = path => readFileSync(new URL(path, root), 'utf8');
test('reference reading themes and typographic preferences remain consistent', () => {
  assert.deepEqual(READER_THEMES, ['paper','warm','sage','night']);
  assert.equal(READER_DEFAULTS.size, 19);
  assert.equal(READER_DEFAULTS.leading, 1.85);
  assert.equal(READER_DEFAULTS.measure, 720);
  assert.equal(normalizeReaderPreferences({size:35}).size, 26);
  assert.equal(normalizeReaderPreferences({size:8}).size, 16);
  assert.equal(normalizeReaderPreferences({theme:'dark'}).theme, 'night');
});
test('Quarto adapter leaves tables, mathematics, search and languages intact', () => {
  const css=read('assets/reader-comfort.css');
  const js=read('assets/reader-comfort.mjs');
  const include=read('assets/includes/reader-comfort.html');
  for (const name of READER_THEMES) assert.ok(css.includes('data-reader-theme="' + name + '"'));
  assert.match(css, /\.quarto-color-scheme-toggle\s*\{\s*display:\s*none\s*!important/);
  assert.ok(css.includes('overflow-x: auto'));
  for (const feature of ['data-reader-focus-input','data-reader-theme-choice','data-reader-size-range','data-reader-reset']) {
    assert.ok(js.includes(feature), 'missing: '+feature);
  }
  assert.match(include, /type="module"/);
});

test('active HTML profile includes reader assets and retains native search', () => {
  const conf=read('_quarto.yml');
  assert.ok(conf.includes('assets/reader-comfort.css'));
  assert.ok(conf.includes('assets/includes/reader-comfort.html'));
  assert.ok(conf.includes('search: true'));
  assert.ok(conf.includes('toc: true'));
  assert.ok(read('assets/includes/reader-comfort.html').includes('/assets/reader-comfort.mjs'));
});

test('public Pages subpath uses Quarto root-relative resource rewriting',()=>{
 const include=read('assets/includes/reader-comfort.html');
 assert.ok(!include.includes('/causal-inference-reader/assets/'));
 assert.match(include,/src="\/assets\/reader-comfort\.mjs"/);
});

test('bookmarks are restricted to this GitHub Pages book, not the shared github.io origin', () => {
  for (const path of ['/causal-inference-reader/', '/causal-inference-reader/manuscript/01-questions.html',
    '/causal-inference-reader/manuscript/01-questions.html#问题']) {
    assert.equal(isCurrentBookPath(path), true, path);
  }
  for (const path of ['/', '//evil.example/path', '/other-book/chapter.html',
    '/causal-inference-reader/../other-book/', '/causal-inference-reader/%2e%2e/other-book/',
    '/causal-inference-reader/%0a', '/causal-inference-reader/%5cpath']) {
    assert.equal(isCurrentBookPath(path), false, path);
  }
  assert.match(read('assets/reader-comfort.mjs'), /causal-inference-reader:' \+ key/);
  assert.match(read('assets/reader-comfort.css'), /bottom: calc\(5rem \+ env\(safe-area-inset-bottom\)\)/);
});
