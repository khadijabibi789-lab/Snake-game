import tkinter as tk
import random


class SnakeGame:
    CELL_SIZE = 20
    COLS = 30
    ROWS = 20
    SPEED = 120

    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            root,
            width=self.COLS * self.CELL_SIZE,
            height=self.ROWS * self.CELL_SIZE,
            bg="black",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.score_var = tk.StringVar(value="Score: 0  |  High: 0")
        self.status_label = tk.Label(
            root, textvariable=self.score_var, font=("Consolas", 12),
            bg="#222", fg="#0f0", pady=4,
        )
        self.status_label.pack(fill=tk.X)

        self.high_score = 0
        self.reset_game()

        self.root.bind("<KeyPress>", self.on_key)
        self.root.bind("<space>", lambda e: self.toggle_pause())

    def reset_game(self):
        cx, cy = self.COLS // 2, self.ROWS // 2
        self.snake = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.score = 0
        self.paused = False
        self.game_over = False
        self.spawn_food()
        self.update_status()
        self.draw()
        self.schedule_step()

    def spawn_food(self):
        while True:
            pos = (random.randint(0, self.COLS - 1), random.randint(0, self.ROWS - 1))
            if pos not in self.snake:
                self.food = pos
                return

    def on_key(self, event):
        key = event.keysym.lower()
        moves = {
            "up": (0, -1), "w": (0, -1),
            "down": (0, 1), "s": (0, 1),
            "left": (-1, 0), "a": (-1, 0),
            "right": (1, 0), "d": (1, 0),
        }
        if key in moves:
            dx, dy = moves[key]
            if (dx, dy) != (-self.direction[0], -self.direction[1]):
                self.next_direction = (dx, dy)
        elif key == "r":
            self.reset_game()

    def toggle_pause(self):
        if not self.game_over:
            self.paused = not self.paused
            if not self.paused:
                self.schedule_step()

    def schedule_step(self):
        if not self.paused and not self.game_over:
            self.root.after(self.SPEED, self.step)

    def step(self):
        if self.paused or self.game_over:
            return
        self.direction = self.next_direction
        head_x = self.snake[0][0] + self.direction[0]
        head_y = self.snake[0][1] + self.direction[1]

        if (
            head_x < 0 or head_x >= self.COLS
            or head_y < 0 or head_y >= self.ROWS
            or (head_x, head_y) in self.snake
        ):
            self.end_game()
            return

        self.snake.insert(0, (head_x, head_y))
        if (head_x, head_y) == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()

        self.update_status()
        self.draw()
        self.schedule_step()

    def end_game(self):
        self.game_over = True
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_status()
        self.canvas.create_text(
            self.COLS * self.CELL_SIZE // 2,
            self.ROWS * self.CELL_SIZE // 2,
            text=f"GAME OVER\nScore: {self.score}\nPress R to restart",
            fill="red", font=("Consolas", 18, "bold"), justify="center",
        )

    def update_status(self):
        state = "PAUSED" if self.paused else ("GAME OVER" if self.game_over else "Playing")
        self.score_var.set(f"Score: {self.score}  |  High: {self.high_score}  |  {state}")

    def draw(self):
        self.canvas.delete("all")
        fx, fy = self.food
        self.canvas.create_rectangle(
            fx * self.CELL_SIZE, fy * self.CELL_SIZE,
            (fx + 1) * self.CELL_SIZE, (fy + 1) * self.CELL_SIZE,
            fill="red", outline="",
        )
        for i, (x, y) in enumerate(self.snake):
            color = "#0f0" if i == 0 else "#0a0"
            self.canvas.create_rectangle(
                x * self.CELL_SIZE, y * self.CELL_SIZE,
                (x + 1) * self.CELL_SIZE, (y + 1) * self.CELL_SIZE,
                fill=color, outline="",
            )


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()