class Solution:
    def simplifyPath(self, path: str) -> str:
        dirList = path.split("/")
        stack = []

        for name in dirList:
            if name == "" or name == ".": continue
            elif name == "..":
                if len(stack) != 0:
                    stack.pop(len(stack) - 1)
                continue
                
            stack.append(name)

        stack.insert(0, "")

        if stack[len(stack) - 1] == ".":
            stack.pop(len(stack) - 1)
        elif stack[len(stack) - 1] == "..":
            for _ in range(2):
                if len(stack) != 0:
                    stack.pop(len(stack) - 1)

        return "/" if len(stack) == 0 or len(stack) == 1 else "/".join(stack)


solution = Solution()
print(solution.simplifyPath("/"))
print(solution.simplifyPath("/home/"))
print(solution.simplifyPath("/home//foo/"))
print(solution.simplifyPath("/home/user/Documente/../Pictures"))
print(solution.simplifyPath("/../"))
print(solution.simplifyPath("/..foo/"))
print(solution.simplifyPath("/fooo../"))
print(solution.simplifyPath("/.../a/../b/c/../d/./"))
print(solution.simplifyPath("/a/../../b/../c//.//"))

# 34ms
# Beats76.93%
# 16.61MB
# Beats20.23%
