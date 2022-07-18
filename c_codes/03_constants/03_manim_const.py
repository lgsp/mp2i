from manim import *
        
class ConstantsFullCode(Scene):
    def construct(self):
        text = Text("03 Constants Full Code", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codeFullCode = Code(
            file_name="03_constants.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(1)
        self.play(Write(codeFullCode), run_time=16)
        self.wait(8)
        
        
class ConstantsAnimation(Scene):
    def construct(self):
        text = Text("02 Constants Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart1 = Code(
            file_name="02_manim_variables_part1.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.75)
        
        self.add(codePart1)
        self.wait(2)

        text = Text("02 Constants Part 2", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart2 = Code(
            file_name="02_manim_variables_part2.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.75)
        
        self.play(ReplacementTransform(codePart1, codePart2), run_time=4)


        text = Text("02 Constants Full Code", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codeFullCode = Code(
            file_name="02_variables.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.5)
        
        self.play(ReplacementTransform(codePart3, codeFullCode), run_time=4)
        self.wait(4)
