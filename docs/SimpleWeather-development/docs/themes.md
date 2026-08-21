---
tags:
  - Themes
  - SimpleWeather
  - correct classes
  - widgets

authors:
  - Afridyne
  - "John Piers Cilliers <https://avatars.githubusercontent.com/u/1306639?s=400&v=4>"
  - SimpleWeather
  - "Roman Lefler <https://github.com/romanlefler/SimpleWeather/blob/development/AUTHORS>"

icon: material/weather-night
---

![Dark Theme](imgs/theme.png){:style="display: block; margin: 0 auto"}
<H1 style="text-align: center;"> Themes - SimpleWeather</H1>

<H4 style="text-align: center;"> Themes are done by dynamically adding the correct classes onto widgets for the chosen theme.</H4>

## Files and Naming

!!! soundcloud "Files and Naming"
    Themes are stored in the `themes/` directory as `<name>.css`.
    
    In order for them to appear in the settings, they must be added to `src/preferences/generalPage.ts` in the themes model and array.
    
    Each class takes the name of `sw-style-<theme>-<class>`.
    
    Example of a "sky" theme in `themes/sky.css`:
    
    ```css
    .sw-style-sky-bg {
        background: #C2DAE6;
    }
    
    .sw-style-sky-forecast-box:hover {
        background: #DAEBF2;
    }
    ```
    
    !!! abstract "NOTE"
    
        **Note!**
        `light` is a good example of a theme.
        
    
### Notes

!!! recommendation "Notes"
    Prefer `background` over `background-color` in case a GTK style uses a background image.
    
### Classes

!!! desc "Classes"
    
    ```
    menu
    |--- bg
    |    |--- left-box
    |    |--- forecast-box
    |    |--- faded
    ```
    
    Additional clases:
    
    ```
    button
    ```
    
### "Attributes"

!!! recommendation "Attributes"
    There are "attribute" classes which show some kind of logic in the program.
    They look like `swa-<name>`.
    Attributes should be in selectors in conjunction with the normal classes.
    
    The `menu` can have the following:
    
    - `open` when pop-up is open
    - any of the following for weather conditions: `clear`, `cloudy`, `rainy`, `snowy`, `stormy`, `windy`
    - either `day` or `night`
    
    For example, this selector makes the faded text yellow on a sunny day:
    
    ```css
    .sw-style-<theme>-menu.swa-clear.swa-day .sw-style-<theme>-faded {
        color: yellow;
    }
    ```
