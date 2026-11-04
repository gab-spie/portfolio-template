// Exporte le portfolio en PDF (français et anglais).
// Utilisation :   npm i playwright,  npx playwright install chromium,  puis  node exporter-pdf.js
// Résultat :      portfolio-fr.pdf et portfolio-en.pdf
// Sans script, tu peux aussi ouvrir la page et faire « Imprimer » > « Enregistrer au format PDF ».
const path = require('path');
const fs = require('fs');
const { pathToFileURL } = require('url');

let chromium;
try {
  ({ chromium } = require('playwright'));
} catch (e) {
  console.error('Playwright est introuvable. Lance d\'abord :  npm i playwright   puis   npx playwright install chromium');
  process.exit(1);
}

// la page ouverte en fichier lit contenu.js : il doit être à jour avec contenu.json
function verifierCopie() {
  const json = path.join(__dirname, 'contenu.json'), js = path.join(__dirname, 'contenu.js');
  if (!fs.existsSync(js)) throw new Error('contenu.js introuvable : lance d\'abord  python3 sync-contenu.py');
  if (fs.existsSync(json) && fs.statSync(json).mtimeMs > fs.statSync(js).mtimeMs + 1000) {
    console.warn('Attention : contenu.json a été modifié après contenu.js. Lance  python3 sync-contenu.py  sinon le PDF montrera l\'ancien contenu.');
  }
}

(async () => {
  verifierCopie();
  const url = pathToFileURL(path.join(__dirname, 'index.html')).href;
  const browser = await chromium.launch();
  try {
    for (const lang of ['fr', 'en']) {
      const ctx = await browser.newContext({ reducedMotion: 'reduce', colorScheme: 'light', viewport: { width: 1280, height: 900 } });
      const page = await ctx.newPage();
      await page.goto(url + '?lang=' + lang);
      // page construite (header.hero) ou message d'erreur de contenu.json
      await page.waitForFunction(() => document.querySelector('header.hero') || /contenu\.json/.test((document.getElementById('contenu') || {}).textContent || ''));
      if (!(await page.$('header.hero'))) {
        throw new Error('la page ne s\'est pas construite : ' + (await page.textContent('#contenu')).trim().slice(0, 200));
      }
      await page.waitForLoadState('load');
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(800);
      await page.emulateMedia({ media: 'print' });
      const out = path.join(__dirname, 'portfolio-' + lang + '.pdf');
      await page.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: '12mm', bottom: '12mm', left: '12mm', right: '12mm' } });
      console.log('OK ' + out);
      await ctx.close();
    }
  } finally {
    await browser.close();
  }
})().catch((e) => {
  console.error('Export PDF impossible : ' + (e && e.message ? e.message : e));
  process.exitCode = 1;
});
