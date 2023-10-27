#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;

void main() {
vec2 st = gl_FragCoord.xy/u_resolution;
    // Step retorna 0 caso o valor seja menor que 0.5,
    // e retorna 1 caso seja maior
    float y = step(0.5,st.x);
    vec3 color = vec3(y,0.45,y); // y varia entre 0 e 1
    gl_FragColor = vec4(color,1.0);
}   