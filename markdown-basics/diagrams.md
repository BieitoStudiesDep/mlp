# MD Diagrams

[doc](https://support.typora.io/Draw-Diagrams-With-Markdown/)

Precondition
Typora supports some Markdown extensions for diagrams, to use this feature, first please enable Diagrams in Preferences Panel → Markdown section.

When exporting as HTML, PDF, epub, docx, those rendered diagrams will also be included, but diagrams features are not supported when exporting markdown into other file formats in current version. Besides, you should also notice that diagrams is not supported by standard Markdown, CommonMark or GFM. Therefore, we still recommend you to insert an image of these diagrams instead of write them in Markdown directly.

Sequence Diagrams
This feature uses js-sequence, which turns the following code block into a rendered diagram:

```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```

js-sequence

For more details, please see this syntax explanation.

Sequence Diagrams Options
You could change CSS variable --sequence-theme to set theme for sequence diagrams, supported value are simple (default) and hand. For example, add following CSS in Custom CSS, and you will get:

:root {
--sequence-theme: hand
}
–sequence-theme: simple –sequence-theme: hand
Screen Shot 2021-04-05 at 23.38.52 Screen Shot 2021-03-13 at 23.56.07
Flowcharts
This feature uses flowchart.js, which turns the following code block into a rendered diagram:

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

flowchart

Mermaid
Typora also has integration with mermaid, which supports sequence diagrams, flowcharts, Gantt charts, class and state diagrams, and pie charts.

Sequence Diagrams
For more details see these instructions.

```mermaid
%% Example of sequence diagram
  sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick
    Bob->>Alice: Not so good :(
    else is well
    Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
    Bob->>Alice: Thanks for asking
    end
```

mermaid-sequence

Flowcharts
For more details see these instructions.

```mermaid
graph LR
A[Hard edge] -->B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

mermaid-flowchart

Gantt Charts
For more details see these instructions.

```mermaid
%% Example with selection of syntaxes
        gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid

        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d

        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d

        section Documentation
        Describe gantt syntax               :active, a1, after des1, 3d
        Add gantt diagram to demo page      :after a1  , 20h
        Add another diagram to demo page    :doc1, after a1  , 48h

        section Last section
        Describe gantt syntax               :after doc1, 3d
        Add gantt diagram to demo page      : 20h
        Add another diagram to demo page    : 48h
```

mermaid-Gantt

Class Diagrams
For more details see these instructions.

```mermaid
classDiagram
      Animal <|-- Duck
      Animal <|-- Fish
      Animal <|-- Zebra
      Animal : +int age
      Animal : +String gender
      Animal: +isMammal()
      Animal: +mate()
      class Duck{
          +String beakColor
          +swim()
          +quack()
      }
      class Fish{
          -int sizeInFeet
          -canEat()
      }
      class Zebra{
          +bool is_wild
          +run()
      }
```

class-diagram

State Diagrams
For more details see these instructions.

```mermaid
stateDiagram
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

state-diagram

Pie Charts

```mermaid
pie
    title Pie Chart
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 150
```

pie-chart

Requirement Diagram
A Requirement diagram provides a visualization for requirements and their connections, to each other and other documented elements. The modeling specs follow those defined by SysML v1.6.

You can find details here.

```mermaid
requirementDiagram

    requirement test_req {
    id: 1
    text: the test text.
    risk: high
    verifymethod: test
    }

    element test_entity {
    type: simulation
    }

    test_entity - satisfies -> test_req
```

Screen Shot 2022-09-06 at 22.03.59

Gitgraph Diagrams / Commit Flow
A Git Graph is a pictorial representation of git commits and git actions(commands) on various branches.

You can find details here.

```mermaid
gitGraph
       commit
       commit
       branch develop
       checkout develop
       commit
       commit
       checkout main
       merge develop
       commit
       commit
```

Screen Shot 2022-08-19 at 16.07.24

C4 Diagrams (plantUML compatible)
Mermaid’s c4 diagram syntax is compatible with plantUML.

You can find details here.

Mindmap
A mind map is a diagram used to visually organize information into a hierarchy, showing relationships among pieces of the whole. It is often created around a single concept, drawn as an image in the center of a blank page, to which associated representations of ideas such as images, words and parts of words are added. Major ideas are connected directly to the central concept, and other ideas branch out from those major ideas.

You can find details here.

```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
```

Screenshot 2023-01-04 at 22.21.05

Timeline
See https://mermaid.js.org/syntax/timeline.html for detail.

Screenshot 2023-05-10 at 22.46.25

Quadrant Chart
See https://mermaid.js.org/syntax/quadrantChart.html for details.

Screenshot 2023-08-20 at 11.53.47

Sankey diagrams
See https://mermaid.js.org/syntax/sankey.html for details.

Screenshot 2023-08-20 at 11.55.40

ZenUML
See https://mermaid.js.org/syntax/zenuml.html for details.

Screenshot 2023-08-29 at 21.13.14

Please notice that zenuml is not first class diagram in mermaid, it may lack some features, like dark themes, etc.

XY Chart
You can find more details here → https://mermaid.js.org/syntax/xyChart.html.

You can now draw charts like this:

Screenshot 2023-12-13 at 19.23.18

Global Mermaid Options
Overview
You can change Mermaid options by adding Custom CSS, supported options include:

:root {
--mermaid-theme: default; /_or base, dark, forest, neutral, night _/
--mermaid-font-family: "trebuchet ms", verdana, arial, sans-serif;
--mermaid-sequence-numbers: off; /_ or "on", see https://mermaid-js.github.io/mermaid/#/sequenceDiagram?id=sequencenumbers_/
--mermaid-flowchart-curve: linear /_ or "basis", see https://github.com/typora/typora-issues/issues/1632_/;
--mermaid--gantt-left-padding: 75; /_ see https://github.com/typora/typora-issues/issues/1665_/
}
Please note that if you export document with other themes than currently used one, some mermaid options will not be applied to exported HTML / PDF / Image. For example, if you currently use them Github, but while export to PDF, you set theme YYY for PDF export, and YYY.css defines --mermaid-sequence-numbers: on, then the --mermaid-sequence-numbers: on would not be applied to exported PDF.

Diagram Alignment
You can add below custom CSS following Add Custom CSS to left align your diagram.

.md-diagram-panel-preview {text-align:left;}
Mermaid Theme
Added --mermaid-theme css variable to quickly define a mermaid theme that fits your theme, the value can be base, default, dark, forest, neutral, night (the one used in night theme), for example:

CSS Mermaid Demo
:root {--mermaid-theme:dark;} Screen Shot 2020-12-05 at 17.08.46
:root {--mermaid-theme:neutral;} Screen Shot 2020-12-05 at 17.09.42
:root {--mermaid-theme:forest;} Screen Shot 2020-12-05 at 17.10.11
Auto Numbering
Add --mermaid-sequence-numbers: on; in Custom CSS will enable auto numbering for sequence in mermaid:

–mermaid-sequence-numbers:off –mermaid-sequence-numbers:on
Screen Shot 2021-04-05 at 23.08.37 Screen Shot 2021-04-05 at 23.20.31
Flowchart Curve
Add --mermaid-flowchart-curve: basis to get other type of curves.

–mermaid-flowchart-curve: linear; –mermaid-flowchart-curve: basis –mermaid-flowchart-curve: natural; –mermaid-flowchart-curve: step;
Screen Shot 2021-04-05 at 23.25.41 Screen Shot 2021-04-05 at 23.30.11 Screen Shot 2021-04-05 at 23.28.06 Screen Shot 2021-04-05 at 23.28.52
Gantt Padding
–mermaid–gantt-left-padding:75 –mermaid–gantt-left-padding:200
Screen Shot 2021-04-05 at 23.33.31 Screen Shot 2021-04-05 at 23.33.00
Inline Mermaid Config
You can add %%{init: [options]}%% in the first line of mermaid diagram to config mermaid details like below:

Screen Shot 2022-08-19 at 16.04.36

You can find full document on https://mermaid-js.github.io/mermaid/#/./directives.

Save-as / Copy on Diagrams
You can right click on a diagram to save it as SVG, PNG or JPG files to your local disk.

Also, you can right click on a diagram to copy it in your clipboard.