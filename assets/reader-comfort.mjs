/**
 * Shared, dependency-free academic reader controls.
 * This is a presentation-only enhancement: source text and editions stay unchanged.
 */
export const READER_DEFAULTS = Object.freeze({
  theme: 'paper', size: 19, leading: 1.85, measure: 720, font: 'serif', focus: false
});
export const READER_THEMES = Object.freeze(['paper', 'warm', 'sage', 'night']);

export function normalizeReaderPreferences(value = {}) {
  const input = value && typeof value === 'object' ? value : {};
  const theme = input.theme === 'dark' ? 'night' : input.theme === 'light' ? 'paper' : input.theme;
  const size = input.size === null || input.size === undefined || input.size === '' ? NaN : Number(input.size);
  return {
    theme: READER_THEMES.includes(theme) ? theme : READER_DEFAULTS.theme,
    size: Number.isFinite(size) ? Math.min(26, Math.max(16, Math.round(size))) : READER_DEFAULTS.size,
    leading: [1.65, 1.85, 2.05].includes(Number(input.leading)) ? Number(input.leading) : READER_DEFAULTS.leading,
    measure: [620, 720, 820].includes(Number(input.measure)) ? Number(input.measure) : READER_DEFAULTS.measure,
    font: input.font === 'sans' ? 'sans' : 'serif',
    focus: input.focus === true || input.focus === 'true'
  };
}

export function readerSearchTarget(href, query, base) {
  const original = new URL(href, base);
  if (original.origin !== new URL(base).origin || !String(query).trim()) return href;
  original.searchParams.set('reader-query', String(query).trim().slice(0, 100));
  return original.pathname + original.search + original.hash;
}

export function readerScopeMatches(entry, scope) {
  if (scope === 'all') return true;
  const url = String(entry?.url || entry?.href || '');
  if (scope === 'book') return /\/book\//.test(url);
  if (scope === 'papers') return /\/(?:papers|appendices)\//.test(url);
  return false;
}

function initReaderComfort() {
  const root = document.documentElement;
  if (!document.body || root.dataset.readerComfortReady) return;
  root.dataset.readerComfortReady = 'true';
  const english = root.dataset.uiLanguage === 'en' || root.lang?.toLowerCase().startsWith('en') ||
    /^\/en(?:\/|$)/.test(location.pathname);
  const t = english ? {
    settings: 'Reading settings', appearance: 'Reading background', fontSize: 'Text size',
    spacing: 'Line spacing', width: 'Text width', font: 'Body font', serif: 'Book serif',
    sans: 'Sans serif', focus: 'Focus mode', reset: 'Restore defaults',
    bookmark: 'Save bookmark', saved: 'Saved bookmarks', continue: 'Continue reading',
    all: 'All', book: 'Book', papers: 'Papers', searchScope: 'Search in',
    themeNames: ['Soft white', 'Warm paper', 'Sage green', 'Night'],
    remove: 'Remove bookmark'
  } : {
    settings: '阅读设置', appearance: '阅读背景', fontSize: '正文字号',
    spacing: '行距', width: '版心宽度', font: '正文字体', serif: '宋体／衬线',
    sans: '黑体／无衬线', focus: '专注模式', reset: '恢复默认',
    bookmark: '添加书签', saved: '我的书签', continue: '继续上次阅读',
    all: '全书', book: '专著', papers: '论文', searchScope: '搜索范围',
    themeNames: ['柔白', '暖纸', '浅绿', '深夜'],
    remove: '删除书签'
  };
  const storage = {
    get(key) { try { return localStorage.getItem(key); } catch { return null; } },
    set(key, value) { try { localStorage.setItem(key, value); } catch {} }
  };
  let saved = null;
  try { saved = JSON.parse(storage.get('reader-preferences-v1') || 'null'); } catch {}
  const initial = saved || {
    theme: storage.get('reading-theme'), size: storage.get('reading-size'),
    focus: storage.get('reading-focus') === 'true'
  };
  let prefs = normalizeReaderPreferences(initial);
  const host = document.querySelector('.topbar .tools');
  const details = document.createElement('details');
  details.className = 'reader-settings' + (host ? '' : ' reader-settings--floating');
  const themes = READER_THEMES.map((key, i) =>
    '<button type="button" class="reader-theme-choice" data-reader-theme-choice="' + key +
    '" aria-pressed="false"><span class="reader-theme-dot reader-theme-dot--' + key +
    '" aria-hidden="true"></span>' + t.themeNames[i] + '</button>'
  ).join('');
  details.innerHTML = [
    '<summary aria-label="' + t.settings + '" title="' + t.settings + '">',
      '<span aria-hidden="true">⚙</span><span class="reader-settings-title">' + t.settings + '</span></summary>',
    '<div class="reader-settings-panel" role="group" aria-label="' + t.settings + '">',
      '<p class="reader-setting-heading">' + t.appearance + '</p>',
      '<div class="reader-theme-options">' + themes + '</div>',
      '<div class="reader-setting-row"><label for="reader-size-input">' + t.fontSize + '</label>',
        '<button type="button" data-reader-size-step="-1" aria-label="A minus">A−</button>',
        '<output data-reader-size-output for="reader-size-input">19px</output>',
        '<button type="button" data-reader-size-step="1" aria-label="A plus">A+</button></div>',
      '<input type="range" id="reader-size-input" data-reader-size-range min="16" max="26" step="1" value="19">',
      '<div class="reader-setting-row"><label for="reader-leading-select">' + t.spacing + '</label>',
        '<select id="reader-leading-select" data-reader-leading>',
          '<option value="1.65">1.65</option><option value="1.85">1.85</option>',
          '<option value="2.05">2.05</option></select></div>',
      '<div class="reader-setting-row"><label for="reader-measure-select">' + t.width + '</label>',
        '<select id="reader-measure-select" data-reader-measure>',
          '<option value="620">620px</option><option value="720">720px</option>',
          '<option value="820">820px</option></select></div>',
      '<div class="reader-setting-row"><label for="reader-font-select">' + t.font + '</label>',
        '<select id="reader-font-select" data-reader-font>',
          '<option value="serif">' + t.serif + '</option>',
          '<option value="sans">' + t.sans + '</option></select></div>',
      '<label class="reader-setting-row"><span>' + t.focus + '</span>',
        '<input type="checkbox" data-reader-focus-input></label>',
      '<div class="reader-setting-actions">',
        '<button type="button" data-reader-add-bookmark>' + t.bookmark + '</button>',
        '<button type="button" data-reader-reset>' + t.reset + '</button></div>',
      '<div class="reader-saved-reading" data-reader-saved-reading></div>',
    '</div>'
  ].join('');
  (host || document.body).append(details);

  const select = (selector) => details.querySelector(selector);
  const lastContainer = select('[data-reader-saved-reading]');
  function currentLocation() {
    const headings = [...document.querySelectorAll(
      'article.content h1[id], article.content h2[id], article.content h3[id], ' +
      'main.content h2[id], main.content h3[id], main.content h4[id]'
    )];
    let heading;
    for (const h of headings) if (h.getBoundingClientRect().top <= 140) heading = h;
    return location.pathname + (heading ? '#' + encodeURIComponent(heading.id) : '');
  }
  function bookmarks() {
    try { const rows = JSON.parse(storage.get('reader-bookmarks-v1') || '[]');
      return Array.isArray(rows) ? rows.filter(row => row && typeof row.path === 'string' &&
        /^\/(?!\/)/.test(row.path) && typeof row.title === 'string').slice(0, 20) : [];
    } catch { return []; }
  }
  function renderSavedReading() {
    lastContainer.replaceChildren();
    const last = (() => { try { return JSON.parse(storage.get('reader-last-location-v1')); } catch { return null; } })();
    if (last && typeof last.path === 'string' && /^\/(?!\/)/.test(last.path) &&
        last.path.split('#')[0] !== location.pathname) {
      const link = document.createElement('a');
      link.href = last.path;
      link.className = 'reader-continue-link';
      link.textContent = t.continue + ' ↗';
      lastContainer.append(link);
    }
    const rows = bookmarks();
    if (!rows.length) return;
    const heading = document.createElement('p');
    heading.className = 'reader-setting-heading';
    heading.textContent = t.saved;
    lastContainer.append(heading);
    for (const entry of rows) {
      const line = document.createElement('div');
      line.className = 'reader-bookmark-row';
      const link = document.createElement('a');
      link.href = entry.path;
      link.textContent = entry.title.slice(0, 90);
      const del = document.createElement('button');
      del.type = 'button';
      del.textContent = '×';
      del.setAttribute('aria-label', t.remove + ': ' + entry.title);
      del.addEventListener('click', () => {
        storage.set('reader-bookmarks-v1', JSON.stringify(bookmarks().filter(row => row.path !== entry.path)));
        renderSavedReading();
      });
      line.append(link, del);
      lastContainer.append(line);
    }
  }
  function apply() {
    root.dataset.readerTheme = prefs.theme;
    root.dataset.readerFont = prefs.font;
    root.dataset.readerFocus = String(prefs.focus);
    // Keep persisted legacy preferences and existing layout CSS compatible.
    root.dataset.theme = prefs.theme === 'night' ? 'dark' : 'light';
    root.dataset.focus = String(prefs.focus);
    root.style.setProperty('--reading-size', prefs.size + 'px');
    root.style.setProperty('--reader-leading', String(prefs.leading));
    root.style.setProperty('--reader-measure', prefs.measure + 'px');
    select('[data-reader-size-range]').value = prefs.size;
    select('[data-reader-size-output]').textContent = prefs.size + 'px';
    select('[data-reader-leading]').value = String(prefs.leading);
    select('[data-reader-measure]').value = String(prefs.measure);
    select('[data-reader-font]').value = prefs.font;
    select('[data-reader-focus-input]').checked = prefs.focus;
    for (const option of details.querySelectorAll('[data-reader-theme-choice]')) {
      option.setAttribute('aria-pressed', String(option.dataset.readerThemeChoice === prefs.theme));
    }
    storage.set('reader-preferences-v1', JSON.stringify(prefs));
    storage.set('reading-size', String(prefs.size));
    storage.set('reading-theme', prefs.theme === 'night' ? 'dark' : 'light');
    storage.set('reading-focus', String(prefs.focus));
  }
  const change = patch => { prefs = normalizeReaderPreferences({...prefs, ...patch}); apply(); };
  details.addEventListener('click', event => {
    const themeButton = event.target.closest('[data-reader-theme-choice]');
    if (themeButton) change({theme: themeButton.dataset.readerThemeChoice});
    const step = event.target.closest('[data-reader-size-step]');
    if (step) change({size: prefs.size + Number(step.dataset.readerSizeStep)});
    if (event.target.closest('[data-reader-reset]')) change(READER_DEFAULTS);
    if (event.target.closest('[data-reader-add-bookmark]')) {
      const path = currentLocation(), title = document.title.slice(0, 100);
      const next = [{path, title}, ...bookmarks().filter(x => x.path !== path)].slice(0, 20);
      storage.set('reader-bookmarks-v1', JSON.stringify(next));
      renderSavedReading();
    }
  });
  select('[data-reader-size-range]').addEventListener('input', e => change({size: Number(e.target.value)}));
  select('[data-reader-leading]').addEventListener('change', e => change({leading: Number(e.target.value)}));
  select('[data-reader-measure]').addEventListener('change', e => change({measure: Number(e.target.value)}));
  select('[data-reader-font]').addEventListener('change', e => change({font: e.target.value}));
  select('[data-reader-focus-input]').addEventListener('change', e => change({focus: e.target.checked}));
  details.addEventListener('keydown', e => {
    if (e.key === 'Escape') { details.open = false; details.querySelector('summary').focus(); }
  });
  document.addEventListener('click', event => {
    if (details.open && !details.contains(event.target)) details.open = false;
  });
  apply();
  renderSavedReading();

  // Existing full-text search engines remain authoritative; only add shortcuts
  // and optional book/paper scope controls for the bespoke index.
  const search = document.querySelector('[data-search]');
  if (search) {
    const wrap = search.closest('.search-wrap');
    if (wrap) {
      const label = document.createElement('label');
      label.className = 'reader-search-scope';
      label.textContent = t.searchScope + ' ';
      const scope = document.createElement('select');
      scope.dataset.searchScope = '';
      for (const [value, title] of [['all',t.all],['book',t.book],['papers',t.papers]]) {
        const option = document.createElement('option'); option.value = value; option.textContent = title;
        scope.append(option);
      }
      label.append(scope); wrap.append(label);
      scope.addEventListener('change', () => search.dispatchEvent(new Event('input', {bubbles: true})));
    }
  }
  document.addEventListener('keydown', event => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      if (search) { event.preventDefault(); search.focus(); search.select(); }
      else {
        const native = document.querySelector('#quarto-search');
        if (native) { event.preventDefault(); native.click(); }
        const field = document.querySelector('.aa-Input');
        if (field) { event.preventDefault(); field.focus(); }
      }
    }
  });
  const main = document.querySelector('article.content, main.content');
  if (main) {
    const progress = document.createElement('div');
    progress.className = 'reader-progress';
    progress.setAttribute('aria-hidden', 'true');
    document.body.prepend(progress);
    let lastPercent = -1, saveTimer = 0;
    const update = () => {
      const length = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      const percent = Math.round(Math.max(0, Math.min(1, window.scrollY / length)) * 100);
      if (percent !== lastPercent) { progress.style.width = percent + '%'; lastPercent = percent; }
      clearTimeout(saveTimer);
      saveTimer = setTimeout(() => {
        storage.set('reader-last-location-v1', JSON.stringify({path: currentLocation(), percent, title: document.title}));
      }, 500);
    };
    window.addEventListener('scroll', update, {passive: true});
    window.addEventListener('resize', update);
    window.addEventListener('pagehide', () => {
      clearTimeout(saveTimer);
      storage.set('reader-last-location-v1', JSON.stringify({
        path: currentLocation(), percent: lastPercent, title: document.title
      }));
    });
    update();
    const query = new URL(location.href).searchParams.get('reader-query');
    if (query && query.trim().length >= 2 && query.length <= 100 &&
        typeof document.createTreeWalker === 'function' && typeof NodeFilter !== 'undefined') {
      const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
      const needle = query.toLocaleLowerCase();
      let node;
      while ((node = walker.nextNode())) {
        const parent = node.parentElement;
        if (!parent || parent.closest('script, style, a, code, pre, svg, mjx-container, .math')) continue;
        const index = (node.textContent || '').toLocaleLowerCase().indexOf(needle);
        if (index < 0) continue;
        // Query and matched substring may differ in Unicode case folding length;
        // never mutate the source node when the boundary is ambiguous.
        if (node.textContent.slice(index, index + query.length).toLocaleLowerCase() !== needle) continue;
        const range = document.createRange();
        range.setStart(node, index); range.setEnd(node, index + query.length);
        const mark = document.createElement('mark'); mark.className = 'reader-search-hit';
        range.surroundContents(mark);
        if (!location.hash) setTimeout(() => mark.scrollIntoView({block: 'center'}), 120);
        break;
      }
    }
  }
}
if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initReaderComfort, {once: true});
  else initReaderComfort();
}
