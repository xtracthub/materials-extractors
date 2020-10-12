docker run \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /Users/tylerskluzacek/Desktop:/output \
--privileged -t --rm \
singularityware/docker2singularity \
039706667969.dkr.ecr.us-east-1.amazonaws.com/xtract-matio
