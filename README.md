# elal-lang
This is a programming language I made which is really basic using hex. I've made an interpreter using python :P. If you want to modify or make your own elal scripts, you need a hex editor. I use HxD as it's simple. You'll find how to code lower.

## ElAl code
  
All scripts in ElAL start with a header:  
`0x31 0xa1`  
if you don't include this header, the script will complain (you can take that part out if you don't want it)

separator (probably will remove to save space):  
`0x00` (can be `0x01` in case of print)

print:  
`0x11` (followed by data you want or use variable followed by variable escape. End with 0x01 instead of 0x00 for no newline)  
  
input:  
`0x12` (varible to assign)


variables (should be defined AFTER code ):  
`0xe0` - `0xef` (followed by value)

variable escape (see print):  
`0xfd`

end:  
`0xff`

comments:

can be made after `0xff` as nothing after `0xff` is read
