# probabilistic_serial_mechanism

<h3>Installation</h3>
        
<pre><code>pip install probabilistic_serial_mechanism</code></pre>
        
<h3>Basic usage</h3>
        
<pre><code># Create a dictionary R with agents as keys and rank order lists as values.
#
#For example:
#
# R = {0: [0,1,2], 1: [2,1,0]}

probabilistic_mechanism(R)</code></pre>
        
<h3>Mathematical background</h3>
       
<p>See <a href="http://faculty.chicagobooth.edu/eric.budish/research/Budish-Che-Kojima-Milgrom-2013-AER.pdf">Budish, Che, Kojima, and Milgrom 2013</a>.</p>

<h3>API</h3>
         
 <pre><code>>>> from probabilistic_serial_mechanism import probabilistic_mechanism
>>> R = {0: [0,1,2], 1: [2,1,0]}
>>> probabilistic_mechanism(R)
{0: array([ 1. ,  0.5,  0. ]), 1: array([ 0. ,  0.5,  1. ])}
>>> </code></pre>
