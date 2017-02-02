from etaprogress.progress import ProgressBar
from etaprogress.components.misc import get_remaining_width, SPINNER


class MctnnProgressBar(ProgressBar):
    """
    Prints the number of images with no and with multiple faces found in addition to the normal
    progress bar.
    """
    def __init__(self, *args, **kwargs):
        super(MctnnProgressBar, self).__init__(*args, **kwargs)
        self.zero_faces = 0
        self.multiple_faces = 0
        self.template += ' {zero}:0|{multiple}:>1'

    def __str__(self):
        """Returns the fully-built progress bar and other data.
        This has been basically copied from the parent class as I have found no elegant solution to append additional
        data to the template using format() otherwise.
        """
        # Partially build out template.
        bar = '{bar}'
        spinner = next(SPINNER)
        if self.undefined:
            numerator = self.str_numerator
            template = self.template.format(numerator=numerator, bar=bar, spinner=spinner,
                                            zero=self.zero_faces, multiple=self.multiple_faces)
        else:
            percent = int(self.percent)
            fraction = self.str_fraction
            eta = self._eta_string or '--:--'
            template = self.template.format(percent=percent, fraction=fraction, bar=bar, eta=eta, spinner=spinner,
                                            zero=self.zero_faces, multiple=self.multiple_faces)

        # Determine bar width and finish.
        width = get_remaining_width(template.format(bar=''), self.max_width or None)
        bar = self.bar.bar(width, percent=self.percent)
        return template.format(bar=bar)
