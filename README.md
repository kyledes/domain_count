# domain_count

The main script file accepts a single argument for the filename of the file to process. 

The file is read line by line with each line passed to an EmailAdress constructor.
EmailAddress abstracts the specifics of validating an email and spliting the local and
domain information. The regex used is a fairly basic pattern it does not perfectly
encapsulate the RFC.

The Domains class contains the results storage and output.  The output is split into
domains that were parsed from valid email adresses and everything else. Parsing the
results like this will allow the process to function while preserving possible
useful data.

Non-unicode data is logged and skipped. Any valid data on the same line as non-unicode
data will be lost.  Python is handling the non-ascii character set email address. I attempted to
isolate the binary data from the email address in the test by reading one byte at a time.
I doing so I thought I would lose the ability to parse non-ascii characters (larger than
 a single byte).  Sadly, that means nightclubHades.org is skipped.

