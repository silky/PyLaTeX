from pylatex import Document, Section, Figure, SubFigure

doc = Document(default_filepath='subfigures')

with doc.create(Section('Showing subfigures')):
    with doc.create(Figure(position='h!')) as kittens:
        with doc.create(SubFigure(position='b',
                                  width=r'0.45\linewidth')) as left_kitten:

            left_kitten.add_image('docs/static/kitten.jpg',
                                  width=r'\linewidth')
            left_kitten.add_caption('Kitten on the left')
        with doc.create(SubFigure(position='b',
                        width=r'0.45\linewidth')) as right_kitten:

            right_kitten.add_image('docs/static/kitten.jpg',
                                   width=r'\linewidth')
            right_kitten.add_caption('Kitten on the right')
        kittens.add_caption("Two kittens")

doc.generate_pdf()
