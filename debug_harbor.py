import threading
import time
import game_ui


def start():
    game_ui.main()


t = threading.Thread(target=start, daemon=True)
t.start()

for _ in range(100):
    if hasattr(game_ui, 'root') and game_ui.root is not None:
        break
    time.sleep(0.05)

print('root_exists', hasattr(game_ui, 'root') and game_ui.root is not None)
if hasattr(game_ui, 'root') and game_ui.root is not None:
    game_ui.change_location('Harbor')
    print('harbor_packed', game_ui.harbor_actions_frame.winfo_ismapped())
    print('children', [child.cget('text') for child in game_ui.harbor_actions_frame.winfo_children() if hasattr(child, 'cget')])
    print('commands', [child.cget('command') is not None for child in game_ui.harbor_actions_frame.winfo_children() if hasattr(child, 'cget')])
    game_ui.root.destroy()
