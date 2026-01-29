import webbrowser
import itertools
import tkinter as tk
from tkinter import ttk

# 1. Hard-coded three keywords (edit these only once)
KEYWORDS = [
    "your first keyword",
    "your second keyword",
    "your third keyword"
]

# 2. Hard-coded specific Amazon India product page URL (edit this only once)
# Example pattern: https://www.amazon.in/dp/ASIN
# Replace with your real product link
AMAZON_PRODUCT_URL = "https://www.amazon.in/dp/XXXXXXXXXX"

# Google search base URL (uses q= for the search query)
GOOGLE_SEARCH_BASE = "https://www.google.com/search?q="

# Iterator to rotate through keywords forever: k1 -> k2 -> k3 -> k1 -> ...
keyword_cycle = itertools.cycle(KEYWORDS)

def open_promo_link():
    """Open Google search with rotating keyword and then the specific Amazon product page."""
    # Get next keyword
    keyword = next(keyword_cycle)

    # Build Google search URL (q parameter holds the search query)
    google_url = GOOGLE_SEARCH_BASE + keyword.replace(" ", "+")

    # Open Google search
    webbrowser.open_new_tab(google_url)

    # Open the specific Amazon India product page
    webbrowser.open_new_tab(AMAZON_PRODUCT_URL)

def main():
    # Simple Tkinter GUI with one button
    root = tk.Tk()
    root.title("Promo Link Rotator")

    root.geometry("400x150")

    label = ttk.Label(
        root,
        text="Click the button to open Google search\nand the Amazon India product page.",
        anchor="center",
        justify="center"
    )
    label.pack(pady=10)

    btn = ttk.Button(root, text="Open promo link", command=open_promo_link)
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
