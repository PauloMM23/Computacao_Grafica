//Ruído de Simplex (Perlin melhorado) em 3D
//Um shader que utiliza ruído simplex em 3D 
//para criar uma textura tridimensional.

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar ruído simplex em 3D
float simplexNoise(vec3 p) {
    return 0.5 + 0.5 * sin(dot(p, vec3(21.9898, 78.233, 45.543)));
}

void main() {
    vec2 uv = gl_FragCoord.xy /u_resolution.xy;

    // Ajuste a escala para controlar a aparência do ruído
    float scale = 5.0;

    // Gere o valor de ruído simplex em 3D
    float simplex = simplexNoise(vec3(uv * scale, u_time));
    gl_FragColor = vec4(vec3(simplex), 1.0);

    gl_FragColor = vec4(vec3(simplex), 1.0);
}
