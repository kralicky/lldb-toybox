#
# Usage:
# > (lldb) command script import <path-to-this-file>
#

import lldb

def __lldb_init_module(debugger, dict):
	# lldb.formatters.Logger._lldb_formatters_debug_level = 2
	# lldb.formatters.Logger._lldb_formatters_debug_filename = "/tmp/lldb-debug.log"
	import lldb_toybox.lib.registry

	import lldb_toybox.libcxx
	import lldb_toybox.abseil

	lldb_toybox.lib.registry.deploy(debugger)
