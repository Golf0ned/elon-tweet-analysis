import io
import pprint

INFILE = "data/nasdaq_screener_1712430924210.csv"
OUTFILE = "data/cleaned_nasdaq.csv"

PPRINT = False


# clean up the data with a script. because we ran out of time and budget.
def main():
    with open(INFILE, 'r') as inStream:
        # pretty print current state
        if PPRINT:
            wordCounts = {}
            for line in inStream:
                cur = line.split(',')[1]
                for word in cur.split(' '):
                    wordCounts[word] = wordCounts.get(word, 0) + 1
            pprint.pp(wordCounts)
            
        # just do the cleaning
        else:
            with open(OUTFILE, 'w') as outStream:
                for line in inStream:
                    split_line = line.split(",")
                    tokenized_name = split_line[1].split(" ")
                    index = min(safeIndex(tokenized_name, 'Inc.'),
                                safeIndex(tokenized_name, 'Inc'),
                                safeIndex(tokenized_name, 'LP'),
                                safeIndex(tokenized_name, '.com'),
                                safeIndex(tokenized_name, 'Company') if safeIndex(tokenized_name, 'Company') == safeIndex(tokenized_name, '(The)') - 1 else len(tokenized_name),
                                safeIndex(tokenized_name, 'Common'),
                                safeIndex(tokenized_name, 'Depositary'),
                                safeIndex(tokenized_name, 'Limited'),
                                safeIndex(tokenized_name, 'Technologies'),
                                safeIndex(tokenized_name, 'Corporation'))
                    concat_str = split_line[0].strip() + "," + " ".join(tokenized_name[0:index]) + "\n"
                    outStream.write(concat_str)

def safeIndex(string, search):
    try:
        return string.index(search)
    except ValueError:
        return len(string)

if __name__ == "__main__":
    main()