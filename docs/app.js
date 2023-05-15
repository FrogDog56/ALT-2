/* my own custom js html injector to avoid pasting the same page over and over */
const regex = /<body[^>]*>((.|[\n\r])*)<\/body>/im;
const pages = {
  0: "intro.html",
  1: "plan.html",
  2: "design.html",
  3: "create.html",
  4: "evaluate.html",
  5: "reflection.html"
}

async function loadHtml() {
  const response = await fetch("pages/" + pages[0]);
  const text = (await response.text()).match(regex);
  document.getElementById("inject").innerHTML = text[0];
}

loadHtml();
