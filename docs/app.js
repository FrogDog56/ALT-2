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

let current_page = 0;

async function load_html() {
  const response = await fetch(`pages/${pages[current_page]}`);
  const text = (await response.text()).match(regex);
  document.getElementById("inject").innerHTML = text[0];
}

async function next_page() {
  if (current_page == 5) {
    current_page = 0;
  } else {
    current_page++;
  }
  load_html();
}

async function goto_page(page) {
  current_page = page;
  load_html();
}

async function heading_click(page, element) {
  goto_page(page);
  element.classList.add("highlight");
}

load_html();
