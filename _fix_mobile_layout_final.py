"""
Fix mobile layout and navigation issues:
1. ADC/CAR-T/Vaccine: Fix sidebar/main flex-direction on mobile.
2. Vaccine: Fix hero text overlap (padding-top).
3. All: Fix anchor links (AI药物设计, 关于我们, 联系我们) by ensuring correct hash parsing and smooth scroll.
4. All: Fix text alignment in nav.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# 1. Update the UNIFIED CSS in the patch script to include layout fixes
PATCH_SCRIPT = os.path.join(HERE, "_patch_mobile_nav_align.py")

NEW_CSS = r"""    /* ─── UNIFIED MOBILE NAV ─── */
    @media (max-width: 768px) {
      .mobile-menu-btn {
        display: block !important;
        flex-shrink: 0 !important;
        margin-left: auto !important;
      }
      .top-header {
        padding: 10px 16px !important;
        flex-wrap: nowrap !important;
        width: 100% !important;
        max-width: 100vw !important;
        left: 0 !important;
        right: 0 !important;
        justify-content: space-between !important;
        box-sizing: border-box !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
      }
      .top-header .slogan { display: none !important; }
      .top-header-nav {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        max-width: 100vw !important;
        min-height: 100vh !important;
        min-height: 100dvh !important;
        height: auto !important;
        background: #ffffff !important;
        flex: none !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        align-items: stretch !important;
        align-content: flex-start !important;
        gap: 0 !important;
        z-index: 10000 !important;
        opacity: 0 !important;
        visibility: hidden !important;
        pointer-events: none !important;
        transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s !important;
        padding: 72px 0 max(24px, env(safe-area-inset-bottom, 0px)) !important;
        overflow-y: auto !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        display: flex !important;
        margin: 0 !important;
        box-sizing: border-box !important;
      }
      .top-header-nav.open {
        opacity: 1 !important;
        visibility: visible !important;
        pointer-events: auto !important;
      }
      body:has(.top-header-nav.open) {
        overflow: hidden !important;
      }
      /* Top-level rows: block + full width (fixes staggered alignment / tiny tap targets). */
      .top-header-nav > a {
        display: block !important;
        flex: 0 0 auto !important;
        align-self: stretch !important;
        width: 100% !important;
        max-width: 100% !important;
        text-align: center !important;
        font-size: 18px !important;
        padding: 16px 20px !important;
        min-height: 48px !important;
        line-height: 1.35 !important;
        border-radius: 0 !important;
        border-bottom: 1px solid #f3f4f6 !important;
        color: #111827 !important;
        background: transparent !important;
        box-shadow: none !important;
        box-sizing: border-box !important;
        -webkit-tap-highlight-color: transparent !important;
      }
      .top-header-nav > a:last-of-type {
        border-bottom: none !important;
        padding-bottom: max(28px, calc(16px + env(safe-area-inset-bottom, 0px))) !important;
      }
      .nav-dropdown {
        width: 100% !important;
        max-width: 100% !important;
        align-self: stretch !important;
        flex: 0 0 auto !important;
        text-align: center !important;
        margin: 0 !important;
      }
      .nav-dropdown > a {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        text-align: center !important;
        font-size: 18px !important;
        padding: 16px 20px !important;
        min-height: 48px !important;
        line-height: 1.35 !important;
        border-radius: 0 !important;
        border-bottom: 1px solid #f3f4f6 !important;
        color: #111827 !important;
        background: transparent !important;
        box-shadow: none !important;
        box-sizing: border-box !important;
        -webkit-tap-highlight-color: transparent !important;
      }
      .nav-dropdown > a::after { content: ' ▾' !important; }
      .nav-close-btn {
        display: flex !important;
        position: absolute !important;
        top: max(12px, env(safe-area-inset-top, 0px)) !important;
        right: max(12px, env(safe-area-inset-right, 0px)) !important;
        background: #f3f4f6 !important;
        border: none !important;
        width: 44px !important;
        height: 44px !important;
        min-width: 44px !important;
        min-height: 44px !important;
        border-radius: 50% !important;
        font-size: 24px !important;
        color: #111827 !important;
        cursor: pointer !important;
        z-index: 10001 !important;
        align-items: center !important;
        justify-content: center !important;
        touch-action: manipulation !important;
      }
      /* Always show submenus on phone so :focus-within/tabindex is not required (fixes first-tap dead links on iOS). */
      .nav-dropdown .dropdown-menu {
        position: static !important;
        transform: none !important;
        opacity: 1 !important;
        visibility: visible !important;
        box-shadow: none !important;
        width: 100% !important;
        background: #f9fafb !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
        border: none !important;
        border-bottom: 1px solid #f3f4f6 !important;
      }
      .nav-dropdown .dropdown-menu a {
        display: block !important;
        font-size: 15px !important;
        padding: 14px 20px !important;
        text-align: left !important;
        border-bottom: 1px solid #f3f4f6 !important;
        min-height: 44px !important;
        box-sizing: border-box !important;
      }
      .nav-dropdown .dropdown-menu a .menu-title { font-size: 15px !important; margin-bottom: 2px !important; }
      .nav-dropdown .dropdown-menu a .menu-desc { font-size: 12px !important; }

      /* --- Layout Fixes for ADC/CAR-T/Vaccine --- */
      .page-wrap { flex-direction: column !important; }
      .sidebar { 
        width: 100% !important; 
        height: auto !important; 
        position: static !important; 
        border-right: none !important; 
        border-bottom: 1px solid #eee !important;
        padding: 20px !important;
      }
      .main { padding: 30px 20px !important; }
      .main h1 { font-size: 32px !important; }
      .main-intro { margin: -30px -20px 30px !important; padding: 30px 20px !important; }
      .hero { padding-top: 100px !important; } /* Fix overlap in Vaccine */
    }
"""

JS_SNIPPET = """
  <script>
    (function() {
      // 1. Sync Nav Active State
      function setNavActive() {
        var hash = window.location.hash || '';
        var homeLink = document.querySelector('.top-header-nav a[href="index.html"]');
        if (homeLink) homeLink.classList.toggle('active', !hash || hash === '#');
        document.querySelectorAll('.top-header-nav a[href*="#"]').forEach(function(a) {
          var href = a.getAttribute('href');
          var anchor = href.includes('#') ? href.split('#')[1] : '';
          a.classList.toggle('active', anchor && hash === '#' + anchor);
        });
      }
      window.addEventListener('hashchange', setNavActive);
      setNavActive();

      // 2. Smooth Scroll for all anchor links
      document.querySelectorAll('.top-header-nav a').forEach(function(a) {
        a.addEventListener('click', function(e) {
          var href = this.getAttribute('href');
          if (!href || href === '#') return;
          var hashIdx = href.indexOf('#');
          if (hashIdx === -1) return; // Regular page link
          
          var targetId = href.substring(hashIdx + 1);
          var targetEl = document.getElementById(targetId);
          
          // If on same page or index.html (main site), handle scroll
          if (targetEl && (window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || href.startsWith('#'))) {
            e.preventDefault();
            document.querySelector('.top-header-nav').classList.remove('open');
            targetEl.scrollIntoView({ behavior: 'smooth' });
            history.pushState(null, null, '#' + targetId);
          }
        });
      });

      // 3. Dropdown Tabindex Sync
      function syncNavDropdownTabindex() {
        var mobile = window.matchMedia('(max-width: 768px)').matches;
        document.querySelectorAll('.top-header-nav .nav-dropdown').forEach(function(el) {
          if (mobile) el.removeAttribute('tabindex');
          else el.setAttribute('tabindex', '0');
        });
      }
      syncNavDropdownTabindex();
      window.addEventListener('resize', syncNavDropdownTabindex);
    })();
  </script>
"""

def main():
    # Update the patch script itself so NEW_CSS is correct
    with open(PATCH_SCRIPT, "r", encoding="utf-8") as f:
        p_content = f.read()
    
    # Find the NEW = r\"\"\" ... \"\"\" block and replace it
    pattern = r'NEW = r"""(.*?)"""'
    p_content = re.sub(pattern, f'NEW = r"""{NEW_CSS}"""', p_content, flags=re.DOTALL)
    with open(PATCH_SCRIPT, "w", encoding="utf-8", newline="\n") as f:
        f.write(p_content)
    print("Updated _patch_mobile_nav_align.py")

    # Run the updated patch script
    os.system(f'conda run -n base python "{PATCH_SCRIPT}"')

    # Now handle the JS injection and cleanup in all HTML files
    for name in os.listdir(HERE):
        if not name.endswith(".html"):
            continue
        path = os.path.join(HERE, name)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove old scripts we might have injected or that are redundant
        # We look for the start of our previous snippets
        content = re.sub(r'<script>\s*\(function\(\) \{\s*function syncNavDropdownTabindex.*?</script>', '', content, flags=re.DOTALL)
        # Also clean up the inline script in index.html/therasik_index.html if present
        content = re.sub(r'function setNavActive\(\).*?document\.querySelectorAll\(\'\.top-header-nav a\'\)\.forEach\(a => \{.*?\}\);\s*', '', content, flags=re.DOTALL)
        
        # Inject the new unified JS before </body>
        if "</body>" in content:
            content = content.replace("</body>", JS_SNIPPET + "\n</body>")
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(content)
            print(f"Updated JS in {name}")

if __name__ == "__main__":
    main()
