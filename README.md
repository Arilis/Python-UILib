# Python UI-Library
#### By ArilisDev

__How to use this library__

1. Download the project
2. Drop the __*ui_lib.py*__ file into your project directory
3. Import the UILib like so, __*import ui_lib*__
4. Your done!

__Functions__

ui_lib.Clear() __*clears the console*__
ui_lib.Center_Amount = __integer__ __*this sets the centering amount*__
ui_lib.TopLines() __*use this for the top of the options/selection box*__
ui_lib.CreateOption(__string__) __*creates an option*__
ui_lib.Credits(__string__) __*displays credits/whatever you put as the credits/footer*__
ui_lib.BottomLines() __*use this for the bottom of the options/selection box*__
ui_lib.Debug() __*displays the amount of time it took to execute the UI Lib / Project*__

__Example Program__

```python
import ui_lib
ui_lib.Center_Amount = 20
ui_lib.Clear()
ui_lib.TopLines()
ui_lib.Title("Python UILib")
ui_lib.CreateOption("(1) Option 1"), ui_lib.CreateOption("(2) Option 2"), ui_lib.CreateOption("(3) Option 3")
ui_lib.Credits("ArilisDev")
ui_lib.BottomLines()
ui_lib.Debug()
```
![Example Output](https://cdn.zuros.info/uploader/files/da6npcvenex1xd8.png)

__Check/Todo List__

- [X] Create initial UI library
- [ ] Automatic centering without using __ui_lib.Center_Amount__
- [ ] Console coloring
- [ ] Console Title
