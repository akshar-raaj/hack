#s = "What is your name?"
#name = raw_input(s)
#print name

import gettext

t = gettext.translation('gettext_example', 'locale', fallback=True)
_ = t.gettext
print _("This message is in the script")