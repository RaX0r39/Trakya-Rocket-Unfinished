#include <iostream>
#include "raylib.h"
#define RAYGUI_IMPLEMENTATION
#include "raygui.h"

#define SCREEN_WIDTH (1600)
#define SCREEN_HEIGHT (1024)
int main(void)
{
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Roket Yer istasyonu");
    SetTargetFPS(144);

    while (!WindowShouldClose())
    {
        BeginDrawing();

        // Fullscreen
        if (IsKeyDown(KEY_LEFT_ALT) && IsKeyPressed(KEY_ENTER)){
            int monitor = GetCurrentMonitor();
            SetWindowSize(GetMonitorWidth(monitor), GetMonitorHeight(monitor));
            ToggleFullscreen();
        }

        if (!IsWindowFullscreen()) {
            SetWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT);
        }

        // Background color
        ClearBackground({20, 10, 30 ,255});

        //Degree text
        int degreenum = 0;
        std::string degree = std::to_string(degreenum);
        const char* text = "Derece: ";
        const Vector2 text_size = MeasureTextEx(GetFontDefault(), text, 30, 1);
        DrawText(text, 10, 10 , 30, RAYWHITE);
        DrawText(degree.c_str(), 20 + text_size.x, 10, 30, RAYWHITE);

        //Feet text
        int feetnum = 0;
        std::string feet = std::to_string(feetnum);
        const char* text2 = "Feet: ";
        const Vector2 text_size2 = MeasureTextEx(GetFontDefault(), text2, 30, 1);
        DrawText(text2, 10, 40 , 30, RAYWHITE);
        DrawText(feet.c_str(), 20 + text_size2.x, 40, 30, RAYWHITE);

        //Speed text
        int speednum = 0;
        std::string speed = std::to_string(speednum);
        const char* text3 = "Speed: ";
        const Vector2 text_size3 = MeasureTextEx(GetFontDefault(), text3, 30, 1);
        DrawText(text3, 10, 70 , 30, RAYWHITE);
        DrawText(speed.c_str(), 20 + text_size3.x, 70, 30, RAYWHITE);

        //acceleration text
        int accelerationnum = 0;
        std::string acceleration = std::to_string(accelerationnum);
        const char* text4 = "Acceleration: ";
        const Vector2 text_size4 = MeasureTextEx(GetFontDefault(), text4, 30, 1);
        DrawText(text4, 10, 100 , 30, RAYWHITE);
        DrawText(acceleration.c_str(), 30 + text_size4.x, 100, 30, RAYWHITE);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}