# domain_count

The main script file (domain_count.py) accepts a single argument for the filename of the file to process.

The file is read line by line with each line passed to an EmailAddress constructor.
EmailAddress abstracts the specifics of validating an email and splitting the local and
domain information. The regex used is a fairly basic pattern, it does not perfectly
encapsulate the RFC.

The Domains class contains the results storage and output.  The output is split into
domains that were parsed from valid email adresses and everything else. Parsing the
results like this will allow the process to function while preserving possible
useful data.

Non-unicode data is logged and skipped. Any valid data on the same line as non-unicode
data will be lost.  Python is handling the non-ascii character set email addresses. I have
an implementation in the test_binary method of the included test suite that removes the
jpeg data and isolates the indifference@nightclubHades.org address.  While this was an
interesting challenge, I did not include it in the implementation as the solution seemed
to specific to jpeg binary data.

I included an empty requirements file in an attempt to indicate there are no module
dependencies.  It is written in python3.


