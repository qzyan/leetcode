class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split("/")
        stack = []
        for folder in folders:
            if not folder:
                continue
            
            if folder not in [".", ".."]:
                stack.append(folder)
            
            if folder == ".":
                continue
            
            if folder == ".." and stack:
                stack.pop()

        return "/" + "/".join(stack)
