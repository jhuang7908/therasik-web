"""Insert mobile nav tabindex sync before </body> on pages that have the header nav but not the snippet."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

SNIPPET = """
  <script>
  (function() {
    function syncNavDropdownTabindex() {
      var mobile = window.matchMedia('(max-width: 768px)').matches;
      document.querySelectorAll('.top-header-nav .nav-dropdown').forEach(function(el) {
        if (mobile) el.removeAttribute('tabindex');
        else el.setAttribute('tabindex', '0');
      });
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', syncNavDropdownTabindex);
    } else {
      syncNavDropdownTabindex();
    }
    window.addEventListener('resize', syncNavDropdownTabindex);
  })();
  </script>
"""


def main():
    needle = "syncNavDropdownTabindex"
    nav = "top-header-nav"
    for name in sorted(os.listdir(HERE)):
        if not name.endswith(".html"):
            continue
        path = os.path.join(HERE, name)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        if nav not in text or needle in text:
            continue
        low = text.lower()
        bi = low.rfind("</body>")
        if bi == -1:
            print("no </body>:", name)
            continue
        text = text[:bi] + SNIPPET + "\n" + text[bi:]
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("injected:", name)


if __name__ == "__main__":
    main()
