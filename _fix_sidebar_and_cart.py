"""Fix mobile sidebar layout to be multi-column for ADC, CAR-T, and Vaccine pages,
and fix the missing content in CAR-T page caused by body max-height.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PATCH_SCRIPT = os.path.join(HERE, "_patch_mobile_nav_align.py")

def fix_cart_page():
    cart_path = os.path.join(HERE, "Therasik_CART_Page.html")
    if not os.path.exists(cart_path):
        return
    with open(cart_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix the typo that hides the whole page
    old_css = "body { max-height: 0; overflow: hidden; transition: max-height 0.3s ease, padding 0.2s ease; padding: 0 20px; background: #f8fafc; border-left: 3px solid var(--primary); }"
    new_css = ".accordion-body { max-height: 0; overflow: hidden; transition: max-height 0.3s ease, padding 0.2s ease; padding: 0 20px; background: #f8fafc; border-left: 3px solid var(--primary); }"
    
    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(cart_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print("Fixed CAR-T page visibility bug.")

def fix_sidebar_css():
    # Update the patch script to inject horizontal flex/multi-column sidebar css
    with open(PATCH_SCRIPT, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_sidebar_css = """      /* --- Layout Fixes for ADC/CAR-T/Vaccine --- */
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
      .hero { padding-top: 100px !important; } /* Fix overlap in Vaccine */"""
      
    new_sidebar_css = """      /* --- Layout Fixes for ADC/CAR-T/Vaccine --- */
      .page-wrap { flex-direction: column !important; }
      .sidebar { 
        width: 100% !important; 
        height: auto !important; 
        position: static !important; 
        border-right: none !important; 
        border-bottom: 1px solid #eee !important;
        padding: 16px !important;
      }
      .sidebar nav {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 8px !important;
      }
      .sidebar nav a {
        flex: 1 1 calc(50% - 8px) !important;
        justify-content: center !important;
        text-align: center !important;
        padding: 8px 12px !important;
        margin-bottom: 0 !important;
        font-size: 13.5px !important;
      }
      .main { padding: 30px 20px !important; }
      .main h1 { font-size: 32px !important; }
      .main-intro { margin: -30px -20px 30px !important; padding: 30px 20px !important; }
      .hero { padding-top: 100px !important; } /* Fix overlap in Vaccine */"""
    
    if old_sidebar_css in content:
        content = content.replace(old_sidebar_css, new_sidebar_css)
        with open(PATCH_SCRIPT, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print("Updated patch script with multi-column sidebar CSS.")
        
        # Run the patch script to apply changes
        os.system(f'conda run -n base python "{PATCH_SCRIPT}"')

if __name__ == "__main__":
    fix_cart_page()
    fix_sidebar_css()
