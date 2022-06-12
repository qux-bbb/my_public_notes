# linux---sed

sed, stream editor, 用来过滤或转换文本。  

```r
# Replace the first occurrence of a regular expression in each line of a file, and print the result:
sed 's/regular_expression/replace/' filename

# Replace all occurrences of an extended regular expression in a file, and print the result:
sed -r 's/regular_expression/replace/g' filename

# Replace all occurrences of a string in a file, overwriting the file (i.e. in-place):
sed -i 's/find/replace/g' filename

# Replace only on lines matching the line pattern:
sed '/line_pattern/s/find/replace/' filename

# Delete lines matching the line pattern:
sed '/line_pattern/d' filename

# Print the first 11 lines of a file:
sed 11q filename
```

来自 tldr  


2022/6/12  
