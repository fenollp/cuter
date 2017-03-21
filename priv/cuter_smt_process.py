import os
import subprocess
from cuter_smt_library import serialize, unserialize


debug = False


if debug:
	filename = "solver.txt"
	if os.path.isfile(filename):
		clog = open(filename, "a")
	else:
		clog = open(filename, "w")


def log(msg = ""):
	if debug:
		clog.write(msg + "\n")


# time limit per solver process in seconds
timeout = 2


def check(arguments):
	try:
		subprocess.check_call(
			arguments,
			stdout=open(os.devnull, "w"),
		)
	except subprocess.CalledProcessError:
		return False
	except OSError:
		return False
	else:
		return True


class Solver:

	def __init__(self, arguments):
		"""
		Create a subprocess using provided program arguments.
		"""
		self.process = subprocess.Popen(
			arguments,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			universal_newlines=True
		)
		log("; " + " ".join(arguments))

	def write(self, stmt):
		line = serialize(stmt)
		self.process.stdin.write(line + "\n")
		log(line)

	def read(self):
		open_cnt = 0
		close_cnt = 0
		lines = []
		while True:
			line = self.process.stdout.readline()[:-1]
			lines.append(line)
			open_cnt += line.count("(")
			close_cnt += line.count(")")
			if open_cnt == close_cnt:
				break;
		smt = "\n".join(lines)
		log(smt)
		if open_cnt == 0 and close_cnt == 0:
			return smt
		return unserialize(smt)

	def check_sat(self):
		self.write(["check-sat"])
		return self.read()

	def get_value(self, *expr):
		self.write(["get-value", list(expr)])
		return self.read()

	def exit(self):
		self.write(["exit"])