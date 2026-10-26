# Model / system card

## Intended use

Learn short-sequence statistics for an artificial motif recognition task without functional genomic claims. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Generate random DNA strings and insert a short arbitrary tag in positive examples. Encode normalized dinucleotide frequencies and train a softmax classifier. Compare with direct tag matching to expose when a simple rule is better.

## Evaluation protocol

Use independent generated sequence sets for training and test. Report ML classification metrics and exact-tag baseline performance.

## Known limits

The tag is an artificial label, not a promoter, binding site or pathogenic motif. Dinucleotide counts lose positional information and may underperform direct matching.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Use a licensed regulatory-sequence benchmark, chromosome or homology-aware splits, reverse-complement handling and position-aware CNN or attention baselines.
