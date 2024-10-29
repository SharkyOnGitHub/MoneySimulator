import tkinter as tk

class MoneySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Simulator")

        # Initialize money, click value, and upgrade values
        self.money = 0
        self.money_per_click = 1
        self.money_per_second = 0
        self.upgrades = {
            "Restaurant": {"cost": 50, "income": 5, "purchased": False},
            "Cafe": {"cost": 150, "income": 15, "purchased": False},
            "Bank": {"cost": 500, "income": 50, "purchased": False},
            "Click Upgrade": {"cost": 100, "income": 1, "purchased": False, "is_click_upgrade": True}
        }

        # Create UI elements
        self.money_label = tk.Label(root, text=f"Money: ${self.money}", font=("Arial", 16))
        self.money_label.pack()

        self.click_button = tk.Button(root, text="Click for Money", command=self.click)
        self.click_button.pack()

        self.upgrade_buttons = {}
        for upgrade_name, upgrade_info in self.upgrades.items():
            button = tk.Button(root, text=f"Buy {upgrade_name} (${upgrade_info['cost']})", command=lambda name=upgrade_name: self.buy_upgrade(name))
            button.pack()
            self.upgrade_buttons[upgrade_name] = button

        self.update_ui()

        # Start auto-money generation
        self.auto_money()

    def click(self):
        self.money += self.money_per_click
        self.update_ui()

    def buy_upgrade(self, upgrade_name):
        upgrade = self.upgrades[upgrade_name]
        if not upgrade["purchased"] and self.money >= upgrade["cost"]:
            self.money -= upgrade["cost"]
            if "is_click_upgrade" in upgrade and upgrade["is_click_upgrade"]:
                self.money_per_click += upgrade["income"]
            else:
                self.money_per_second += upgrade["income"]
            upgrade["purchased"] = True
            self.update_ui()

    def update_ui(self):
        self.money_label.config(text=f"Money: ${self.money}")
        for upgrade_name, upgrade_info in self.upgrades.items():
            button = self.upgrade_buttons[upgrade_name]
            if upgrade_info["purchased"]:
                button.config(state=tk.DISABLED)
            else:
                button.config(text=f"Buy {upgrade_name} (${upgrade_info['cost']})")

    def auto_money(self):
        self.money += self.money_per_second
        self.update_ui()
        self.root.after(1000, self.auto_money)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    game = MoneySimulator(root)
    root.mainloop()
