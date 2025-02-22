# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
import argparse
from tqdm import tqdm

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
    help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()

predictions = []
for line in tqdm(open(args.eval_corpus_path, encoding='utf-8')):
    predictions.append("London")

total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
if total > 0:
    print('Correct London: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
    print('Predictions written to {}; no targets provided'.format(args.outputs_path))
