# (C) Copyright 2004-2021 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

"""
Implementation of a ButtonEditor demo plugin for Traits UI demo program.

This demo shows each of the two styles of the ButtonEditor.
(As of this writing, they are identical.)
"""

from traits.api import HasTraits, Button
from traitsui.api import Item, View, Group, message


# -------------------------------------------------------------------------
#  Demo Class
# -------------------------------------------------------------------------

class ButtonEditorDemo(HasTraits):
    """ This class specifies the details of the ButtonEditor demo.
    """

    # To demonstrate any given Trait editor, an appropriate Trait is required.
    fire_event = Button('Click Me')

    def _fire_event_fired():
        message("Button clicked!")

    # ButtonEditor display
    # (Note that Text and ReadOnly versions are not applicable)
    event_group = Group(
        Item('fire_event', style='simple', label='Simple', id="simple"),
        Item('_'),
        Item('fire_event', style='custom', label='Custom', id="custom"),
        Item('_'),
        Item(label='[text style unavailable]'),
        Item('_'),
        Item(label='[readonly style unavailable]')
    )

    # Demo view
    traits_view = View(
        event_group,
        title='ButtonEditor',
        buttons=['OK'],
        width=250
    )


# Create the demo:
demo = ButtonEditorDemo()

# Run the demo (if invoked from the command line):
if __name__ == '__main__':
    demo.configure_traits()
