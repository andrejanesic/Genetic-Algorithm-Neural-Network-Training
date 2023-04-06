#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double x_r[50] = {
    0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90,
    1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80, 1.90,
    2.00, 2.10, 2.20, 2.30, 2.40, 2.50, 2.60, 2.70, 2.80, 2.90,
    3.00, 3.10, 3.20, 3.30, 3.40, 3.50, 3.60, 3.70, 3.80, 3.90,
    4.00, 4.10, 4.20, 4.30, 4.40, 4.50, 4.60, 4.70, 4.80, 4.90
};

double y_g[50] = {
    1.0000, 2.2667, 3.5533, 4.8599, 6.1865, 7.5332, 8.8998, 10.2865, 11.6931, 13.1197,
    14.5664, 16.0330, 17.5196, 19.0263, 20.5529, 22.0996, 23.6662, 25.2528, 26.8595, 28.4861,
    30.1327, 31.7994, 33.4860, 35.1927, 36.9193, 38.6659, 40.4326, 42.2192, 44.0258, 45.8525,
    47.6991, 49.5657, 51.4524, 53.3590, 55.2857, 57.2323, 59.1989, 61.1856, 63.1922, 65.2188,
    67.2655, 69.3321, 71.4188, 73.5254, 75.6520, 77.7987, 79.9653, 82.1519, 84.3586, 86.5852
};

// one neuron
double calc_neuron(int neurons, double input_weights[], double input_values[], double bias) {
	int i, j;
	double sum = bias;
	for (i = 0; i < neurons; i++) {
		sum += input_weights[i] * input_values[i];
	}
	return sum;
}

// calc net

#define L1N 4
#define L2N 4

double layer1[L1N][1];
double layer2[L2N][L1N];
double layer3[1][L2N];

double bias1[L1N];
double bias2[L2N];
double bias3[1];

double output0[1];
double output1[L1N];
double output2[L2N];

int main(int argc, char* argv[]) {
    double *y_r = y_g;

    int total_expected_args = 1 + L1N + L1N * L2N + L2N + L1N + L2N + 1;
    if (argc != total_expected_args) {
        // broj argumenata nije odgovarajuci
        fprintf(stderr, "Broj argumenata nije odgovarajuci, ocekivano %d realnih vrednosti.\n", total_expected_args - 1);
        exit(1);
    }

    // parsiranje
    int i, j, k, ai = 1;
    // layer1
    for (i = 0; i < L1N; i++, ai++) {
        layer1[i][0] = atof(argv[ai]);
    }
    // layer2
    for (i = 0; i < L2N; i++) {
        for (j = 0; j < L1N; j++, ai++) {
            layer2[i][j] = atof(argv[ai]);
        }
    }
    // layer3
    for (i = 0; i < L2N; i++) {
        layer3[0][i] = atof(argv[ai]);
    }
    // bias1
    for (i = 0; i < L1N; i++, ai++) {
        bias1[i] = atof(argv[ai]);
    }
    // bias2
    for (i = 0; i < L2N; i++, ai++) {
        bias2[i] = atof(argv[ai]);
    }
    // bias3
    bias3[0] = atof(argv[ai]);

    // idemo dalje!
    double mse = 0;

    for (k = 0; k < 50; k++) {
        output0[0] = x_r[k];
        // layer1
        for (i = 0; i < L1N; i++) {
            output1[i] = calc_neuron(1, layer1[i], output0, bias1[i]);
        }
        // layer2
        for (i = 0; i < L2N; i++) {
            output2[i] = calc_neuron(L1N, layer2[i], output1, bias2[i]);
        }
        // layer3
        double val = calc_neuron(L2N, layer3[0], output2, bias3[0]);

        double err = pow(y_r[k] - val, 2);
        mse += err;
    }

    printf("%.5f\n", mse / 50);
    return 0;
}


