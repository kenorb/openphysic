#!/usr/bin/env bash

minimal_width=2000

rm temp2/png/*.png
for f in temp/png/*.png
do
  read -r width height <<< $( convert $f -format "%w %h" info:)
  width2=$(( ${width} / 2 ))
  height2=${height}
  if [ $width -gt $minimal_width ]; then
    echo "split $f ${width}x${height} to 2 files ${width2}x${height2}"
    f2=$(basename $f)
    convert $f -crop ${width2}x${height2}+0+0 +repage temp2/png/${f2%%.*}a.png
    convert $f -crop ${width2}x${height2}+$width2+0 +repage temp2/png/${f2%%.*}b.png
  else
    echo "copy $f ${width}x${height} (don't split because width<$minimal_width)"
    cp $f temp2/$f
  fi
done