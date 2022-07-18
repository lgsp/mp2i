from manim import *

class OperatorsPart1(Scene):
    def construct(self):
        text = Text("05 Operators Part 1 + - *", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart1 = Code(
            file_name="05_manim_op_part1.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(1)
        self.play(Write(codePart1), run_time=16)
        self.wait(8)

class OperatorsPart2(Scene):
    def construct(self):
        text = Text("05 Operators Reminder Of Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)

        codePart1 = Code(
            file_name="05_manim_op_part1.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(0.8)
        self.play(Write(codePart1), run_time=2)
        self.wait(2)
        self.remove(codePart1)
        
        text = Text("05 Operators Part 2 / %", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart2 = Code(
            file_name="05_manim_op_part2.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(0.85)
        
        self.play(ReplacementTransform(codePart1, codePart2), run_time=4)
        self.wait(8)



class OperatorsPart3(Scene):
    def construct(self):
        text = Text("05 Operators Reminder Of Part 2", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)

        codePart2 = Code(
            file_name="05_manim_op_part2.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(0.85)
        self.play(Write(codePart2), run_time=2)
        self.wait(2)
        self.remove(codePart2)
        
        text = Text("05 Operators Part 3 ++ --", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart3 = Code(
            file_name="05_manim_op_part3.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(1)
        
        self.play(ReplacementTransform(codePart2, codePart3), run_time=4)
        self.wait(8)
        

class OperatorsPart4(Scene):
    def construct(self):
        text = Text("05 Operators Reminder Of Part 3", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)

        codePart3 = Code(
            file_name="05_manim_op_part3.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(1)
        self.play(Write(codePart3), run_time=2)
        self.wait(2)
        self.remove(codePart3)
        
        text = Text("05 Operators Part 4 sizeof", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart4 = Code(
            file_name="05_manim_op_part4.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(0.8)
        
        self.play(ReplacementTransform(codePart3, codePart4), run_time=4)
        self.wait(8)
        
        
        
class OperatorsFullCode(Scene):
    def construct(self):
        text = Text("05 Operators Full Code", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codeFullCode = Code(
            file_name="05_operators.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.5)
        self.play(Write(codeFullCode), run_time=16)
        self.wait(8)
        
        
class OperatorsAnimation(Scene):
    def construct(self):
        text = Text("05 Operators Part 1", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart1 = Code(
            file_name="05_manim_op_part1.c",
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

        text = Text("05 Operators Part 2", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart2 = Code(
            file_name="05_manim_op_part2.c",
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

        text = Text("05 Operators Part 3", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart3 = Code(
            file_name="05_manim_op_part3.c",
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

        text = Text("05 Operators Part 4", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)
        
        codePart4 = Code(
            file_name="05_manim_op_part4.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        )
        
        self.play(ReplacementTransform(codePart3, codePart4), run_time=4)
        self.wait(8)
        
        text = Text("05 Operators Full Code", font = "Monaco")
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.remove(text)

        
        
        codeFullCode = Code(
            file_name="05_operators.c",
            tab_width = 4,
            background_stroke_width = 1,
            background_stroke_color = WHITE,
            insert_line_no = True,
            style = "emacs",
            background = "window",
            language = "c",
            font = "Monaco",
        ).scale(.5)
        
        self.play(ReplacementTransform(codePart4, codeFullCode), run_time=4)
        self.wait(4)
