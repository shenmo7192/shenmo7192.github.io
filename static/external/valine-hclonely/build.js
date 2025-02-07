const yaml = require('js-yaml');
const fs = require('fs');
const { minify } = require("uglify-js");

// Get document, or throw exception on error
try {
  const rules = yaml.load(fs.readFileSync('rules.yml'));
  let valineJsRaw = fs.readFileSync('raw/Valine.format.js').toString();
  for (const [name, rule] of Object.entries(rules)) {
    if (!valineJsRaw.includes(rule.raw)) {
      console.log('Can not find: ' + name);
      return;
    }
    valineJsRaw = valineJsRaw.replace(rule.raw, rule.changed);
  }
  fs.writeFileSync('raw/Valine.changed.js', valineJsRaw);
  const valineJsChanged = minify(valineJsRaw, {
    output: {
      comments: true,
      beautify: false,
      ascii_only: true
    }
  });
  //console.log(valineJsChanged)
  fs.writeFileSync('dist/Valine.min.js', valineJsChanged.code.replace(' */', ' * Modify by HCLonely\n */'));
} catch (e) {
  console.log(e);
}
