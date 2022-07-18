from manim import *

class VariablesPart1(Scene):
    def construct(self):
        text = Text("02 Variables Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart1 = Code(
            file_name="02_manim_var_part1_int.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        )
        self.play(Write(codePart1), run_time=16)
        self.wait(8)

class VariablesPart2(Scene):
    def construct(self):
        text = Text("02 Variables Reminder Of Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)

        codePart1 = Code(
            file_name="02_manim_var_part1_int.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        )
        self.play(Write(codePart1), run_time=2)
        self.wait(2)
        self.remove(codePart1)
        
        text = Text("02 Variables Part 2", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart2 = Code(
            file_name="02_manim_var_part2_float.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        )
        
        self.play(ReplacementTransform(codePart1, codePart2), run_time=4)
        self.wait(8)
        

class VariablesPart3(Scene):
    def construct(self):
        text = Text("02 Variables Reminder Of Part 2", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)

        codePart2 = Code(
            file_name="02_manim_var_part2_float.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        )
        self.play(Write(codePart2), run_time=2)
        self.wait(2)
        self.remove(codePart2)
        
        text = Text("02 Variables Part 3 (Last Part)", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart3 = Code(
            file_name="02_manim_var_part3_char.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        )
        
        self.play(ReplacementTransform(codePart2, codePart3), run_time=4)
        self.wait(8)        

        
class VariablesFullCode(Scene):
    def construct(self):
        text = Text("02 Variables Full Code", font = "Monaco")
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
        ).scale(.55)
        self.play(Write(codeFullCode), run_time=16)
        self.wait(8)
        
        
class VariablesAnimation(Scene):
    def construct(self):
        text = Text("02 Variables Part 1", font = "Monaco")
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

        text = Text("02 Variables Part 2", font = "Monaco")
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


        text = Text("02 Variables Full Code", font = "Monaco")
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
