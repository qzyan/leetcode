class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split("/")
        stack = []
        for folder in folders:
            if not folder:
                continue
            
            if folder == ".":
                continue
            
            if folder == ".." and stack:
                stack.pop()
            else:
                stack.append(folder)

        return "/" + "/".join(stack)
