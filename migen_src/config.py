config = {
	"bit_depth" : 12,
	"pixels_per_cycle": 4,
	"LJ92_fifo_depth": 128,
	"out_bits": 32,
	"converter" : 48,
	"converter_fifo_depth": 256,
	"vbits_to_cbits_buffer_size": 144,
	"predictor_function": 1,
	"num_of_components": 4,
}
'''
bit_depth: is the maximum bit depth supported by the encoder, you can always use lower than that.
this must be between 2 and 16 and should be set as small as possible.
pixels_per_cycle: parallelism level of the encoder, every stage will be repeated for every pixel
and some stages will need bigger buffers for more pixels, so this should be minimum as well.
out_bits: is the number of bits packed and produced by the encoder, the number of the bits is
correlated with the buffer size, so use the least number that will satisfy the throughput needed.
converter: 
vbits_to_cbits_buffer_size: max(3*converter, converter+out_bits)
'''