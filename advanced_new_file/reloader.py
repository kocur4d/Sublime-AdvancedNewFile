# Adapted from @wbond's resource loader.

import sys
import sublime

VERSION = int(sublime.version())

mod_prefix = "advanced_new_file"
reload_mods = []

if VERSION > 3000:
    mod_prefix = "AdvancedNewFile." + mod_prefix
    from imp import reload
    for mod in sys.modules:
        if mod[0:15] == 'AdvancedNewFile' and sys.modules[mod] is not None:
            reload_mods.append(mod)
else:

    for mod in sorted(sys.modules):
        if mod[0:17] == 'advanced_new_file' and sys.modules[mod] is not None:
            reload_mods.append(mod)

mods_load_order = [
    '.anf_util',
    '.anf_base',
    '.completion_base',
    '.nix_platform',
    '.anf_windows_platform',
    '.anf_new'
]

for suffix in mods_load_order:
    mod = mod_prefix + suffix
    if mod in reload_mods:
        reload(sys.modules[mod])