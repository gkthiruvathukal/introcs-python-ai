import os
from collections import deque
from typing import Optional


# start: handler_base
class FileSystemEventWalker:
    """Base handler for filesystem tree-walk events.

    Override any methods you need.  Return False from enter_dir to
    skip a subtree without raising an error.
    """
    def enter_dir(self, path: str, depth: int) -> Optional[bool]:
        pass

    def leave_dir(self, path: str, depth: int) -> None:
        pass

    def visit_file(self, path: str, depth: int) -> None:
        pass

    def error(self, path: str, depth: int, exc: Exception) -> None:
        pass
# end: handler_base


# start: walk_dfs
def walk_dfs(path: str, handler: FileSystemEventWalker, depth: int = 0) -> None:
    """Depth-first recursive traversal rooted at path."""
    try:
        if not os.path.isdir(path):
            handler.visit_file(path, depth)
            return
        if handler.enter_dir(path, depth) is False:
            return
        for name in sorted(os.listdir(path)):
            child = os.path.join(path, name)
            if os.path.isdir(child) and not os.path.islink(child):
                walk_dfs(child, handler, depth + 1)
            else:
                try:
                    handler.visit_file(child, depth + 1)
                except Exception as exc:
                    handler.error(child, depth + 1, exc)
        handler.leave_dir(path, depth)
    except Exception as exc:
        handler.error(path, depth, exc)
# end: walk_dfs


# start: print_handler
class PrintHandler(FileSystemEventWalker):
    """Prints every entry indented by its depth in the tree."""
    def enter_dir(self, path: str, depth: int) -> None:
        print("  " * depth + f"[{os.path.basename(path)}/]")

    def visit_file(self, path: str, depth: int) -> None:
        print("  " * depth + os.path.basename(path))
# end: print_handler


# start: walk_bfs
def walk_bfs(root: str, handler: FileSystemEventWalker) -> None:
    """Breadth-first iterative traversal rooted at root."""
    queue = deque([(root, 0)])
    while queue:
        path, depth = queue.popleft()
        try:
            if not os.path.isdir(path):
                handler.visit_file(path, depth)
                continue
            if handler.enter_dir(path, depth) is False:
                continue
            for name in sorted(os.listdir(path)):
                child = os.path.join(path, name)
                if os.path.isdir(child) and not os.path.islink(child):
                    queue.append((child, depth + 1))
                else:
                    try:
                        handler.visit_file(child, depth + 1)
                    except Exception as exc:
                        handler.error(child, depth + 1, exc)
            handler.leave_dir(path, depth)
        except Exception as exc:
            handler.error(path, depth, exc)
# end: walk_bfs


if __name__ == '__main__':
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    walk_dfs(root, PrintHandler())
