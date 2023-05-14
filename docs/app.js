/* my own custom js html injector to avoid pasting the same page over and over */
const regex_pattern = /<body[^>]*>((.|[\n\r])*)<\/body>/im;

async function loadHtml() {
  const response = await fetch("pages/introduction.html");
  const text = (await response.text()).match(regex_pattern);
  document.getElementById("inject").innerHTML = text[0];
}

loadHtml();
