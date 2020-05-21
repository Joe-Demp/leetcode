# A script to copy files from an IntelliJ project on my computer to this git repo
Copy-Item -Path "C:\Users\demps\IntelliJProjects\Experiments\src\leetcode" -Destination "C:\Users\demps\Documents\Code\leetcode\IntelliJ" -Recurse

# todo include an extra script to do an automated commit of IntelliJ files (only, and if required)
# todo Logging?
