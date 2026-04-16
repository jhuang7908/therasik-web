# One-off: replace legacy UNIFIED MOBILE NAV with viewport-safe rules; insert once before last </style>.
import os

HERE = os.path.dirname(os.path.abspath(__file__))

OLD = r"""    /* ─── UNIFIED MOBILE NAV ─── */
    @media (max-width: 768px) {
      .mobile-menu-btn { display: block !important; }
      .top-header { 
        padding: 10px 16px !important; 
        flex-wrap: nowrap !important; 
        width: 100% !important; 
        left: 0 !important; 
        right: 0 !important; 
        justify-content: space-between !important;
      }
      .top-header .slogan { display: none !important; }
      .top-header-nav { 
        position: fixed !important; 
        top: 0 !important; 
        left: 0 !important; 
        right: 0 !important; 
        width: 100% !important; 
        height: 100vh !important; 
        background: #ffffff !important; 
        flex-direction: column !important; 
        justify-content: center !important; 
        align-items: center !important; 
        gap: 0 !important; 
        z-index: 10000 !important; 
        opacity: 0 !important; 
        visibility: hidden !important;
        pointer-events: none !important; 
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important; 
        padding: 80px 20px 40px !important; 
        overflow-y: auto !important;
        display: flex !important;
        margin: 0 !important;
      }
      .top-header-nav.open { 
        opacity: 1 !important; 
        visibility: visible !important;
        pointer-events: auto !important; 
      }
      .top-header-nav a { 
        font-size: 18px !important; 
        padding: 16px 20px !important; 
        width: 100% !important;
        text-align: center !important;
        border-radius: 0 !important;
        border-bottom: 1px solid #f3f4f6 !important;
        color: #111827 !important;
        background: transparent !important;
        box-shadow: none !important;
      }
      .top-header-nav a:last-child { border-bottom: none !important; }
      .nav-close-btn { 
        display: block !important; 
        position: absolute !important; 
        top: 16px !important; 
        right: 16px !important; 
        background: #f3f4f6 !important; 
        border: none !important; 
        width: 40px !important;
        height: 40px !important;
        border-radius: 50% !important;
        font-size: 24px !important; 
        color: #111827 !important; 
        cursor: pointer !important; 
        z-index: 10001 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
      }
      .nav-dropdown { width: 100% !important; }
      .nav-dropdown > a::after { content: ' ▾' !important; }
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
        display: none !important;
        border: none !important;
        border-bottom: 1px solid #f3f4f6 !important;
      }
      .nav-dropdown:focus-within .dropdown-menu,
      .nav-dropdown:hover .dropdown-menu {
        display: block !important;
      }
      .nav-dropdown .dropdown-menu a {
        font-size: 15px !important;
        padding: 12px 24px !important;
        text-align: left !important;
        border-bottom: 1px solid #f3f4f6 !important;
      }
      .nav-dropdown .dropdown-menu a .menu-title { font-size: 15px !important; margin-bottom: 2px !important; }
      .nav-dropdown .dropdown-menu a .menu-desc { font-size: 12px !important; }
    }
"""

NEW = r"""    /* ─── UNIFIED MOBILE NAV ─── */
    @media (max-width: 768px) {
      /* Full-screen overlay anchored to the viewport (avoid clipping from header filter/stacking). */
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
        justify-content: center !important;
        align-items: stretch !important;
        gap: 0 !important;
        z-index: 10000 !important;
        opacity: 0 !important;
        visibility: hidden !important;
        pointer-events: none !important;
        transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s !important;
        padding: 80px 0 40px !important;
        overflow-y: auto !important;
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
      .top-header-nav a {
        font-size: 18px !important;
        padding: 16px 20px !important;
        width: 100% !important;
        max-width: 100% !important;
        text-align: center !important;
        border-radius: 0 !important;
        border-bottom: 1px solid #f3f4f6 !important;
        color: #111827 !important;
        background: transparent !important;
        box-shadow: none !important;
        box-sizing: border-box !important;
      }
      .top-header-nav a:last-child { border-bottom: none !important; }
      .nav-close-btn {
        display: flex !important;
        position: absolute !important;
        top: max(12px, env(safe-area-inset-top, 0px)) !important;
        right: max(12px, env(safe-area-inset-right, 0px)) !important;
        background: #f3f4f6 !important;
        border: none !important;
        width: 40px !important;
        height: 40px !important;
        border-radius: 50% !important;
        font-size: 24px !important;
        color: #111827 !important;
        cursor: pointer !important;
        z-index: 10001 !important;
        align-items: center !important;
        justify-content: center !important;
      }
      .nav-dropdown { width: 100% !important; max-width: 100% !important; }
      .nav-dropdown > a::after { content: ' ▾' !important; }
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
        display: none !important;
        border: none !important;
        border-bottom: 1px solid #f3f4f6 !important;
      }
      .nav-dropdown:focus-within .dropdown-menu,
      .nav-dropdown:hover .dropdown-menu {
        display: block !important;
      }
      .nav-dropdown .dropdown-menu a {
        font-size: 15px !important;
        padding: 12px 24px !important;
        text-align: left !important;
        border-bottom: 1px solid #f3f4f6 !important;
      }
      .nav-dropdown .dropdown-menu a .menu-title { font-size: 15px !important; margin-bottom: 2px !important; }
      .nav-dropdown .dropdown-menu a .menu-desc { font-size: 12px !important; }
    }
"""


def main():
    for name in os.listdir(HERE):
        if not name.endswith(".html"):
            continue
        path = os.path.join(HERE, name)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        original = content
        if OLD not in content:
            continue
        while OLD in content:
            content = content.replace(OLD, "")
        pos = content.rfind("</style>")
        if pos == -1:
            content = original
            print(f"skip (no </style>): {name}")
            continue
        content = content[:pos] + NEW + "\n  " + content[pos:]
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"updated: {name}")


if __name__ == "__main__":
    main()
