from manim import *

class HelloPart1(Scene):
    def construct(self):
        text = Text("01 Hello Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart1 = Code(
            file_name="01_manim_hello_part1.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = Code.styles_list[15],
            background = "window",
            language = "c",
            font = "Monaco",
        )
        self.play(Write(codePart1), run_time=16)
        self.wait(8)

class HelloPart2(Scene):
    def construct(self):
        text = Text("01 Hello Reminder Of Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)

        codePart1 = Code(
            file_name="01_manim_hello_part1.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = Code.styles_list[15],
            background = "window",
            language = "c",
            font = "Monaco",
        )
        self.play(Write(codePart1), run_time=2)
        self.wait(2)
        
        text = Text("01 Hello Part 2 (Last Part)", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart2 = Code(
            file_name="01_manim_hello_part2.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = Code.styles_list[15],
            background = "window",
            language = "c",
            font = "Monaco",
        )
        
        self.play(ReplacementTransform(codePart1, codePart2), run_time=4)
        self.wait(8)
        


class HelloFullCode(Scene):
    def construct(self):
        text = Text("01 Hello Full Code", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codeFullCode = Code(
            file_name="01_hello.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.85)
        self.play(Write(codeFullCode), run_time=16)
        self.wait(8)
        
        
class HelloAnimation(Scene):
    def construct(self):
        text = Text("01 Hello Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart1 = Code(
            file_name="01_manim_hello_part1.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = Code.styles_list[15],
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.75)
        
        self.add(codePart1)
        self.wait(2)

        text = Text("01 Hello Part 2", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart2 = Code(
            file_name="01_manim_hello_part2.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = Code.styles_list[15],
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.75)
        
        self.play(ReplacementTransform(codePart1, codePart2), run_time=4)


        text = Text("01 Hello Full Code", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codeFullCode = Code(
            file_name="01_hello.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = Code.styles_list[15],
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.5)
        
        self.play(ReplacementTransform(codePart3, codeFullCode), run_time=4)
        self.wait(4)
