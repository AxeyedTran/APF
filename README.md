# APF

Admin Panel Finder

# This Tool Help You Find Admin Panel Of A Website 

### Usages
- Check all paths with php extension
```
python breacher -u example.com --type php
```
- Check all paths with php extension with threads
```
python breacher -u example.com --type php --fast
```
- Check all paths without threads
```
python breacher -u example.com
```
- Adding a custom path. For example if you want all paths to start with /data (example.com/data/...) you can do this:
```
python breacher -u example.com --path /data
```
