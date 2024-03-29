﻿# TIL

## Metal Framework

Metal by Tutoials 읽고, ios의 gpu 가속 연산이 어떻게 이뤄지는지 개괄적으로 학습

```swift
import PlaygroundSupport
import MetalKit


guard let device = MTLCreateSystemDefaultDevice() else {
 fatalError("GPU is not supported")
}
print(device)

let frame = CGRect(x: 0, y: 0, width: 300, height: 300)
let view = MTKView(frame: frame, device: device)
view.clearColor = MTLClearColor(red: 1, green: 0.5, blue: 0.8,
alpha: 1)

// 1
let allocator = MTKMeshBufferAllocator(device: device)
// 2
let mdlMesh = MDLMesh(sphereWithExtent: [1, 0.75, 0.75],
// 3
segments: [100, 100],
inwardNormals: false,
geometryType: .triangles,
allocator: allocator)
let mesh = try MTKMesh(mesh: mdlMesh, device: device)

guard let commandQueue = device.makeCommandQueue() else {
fatalError("Could not create a command queue")
}

    
let shader = """
#include <metal_stdlib>
using namespace metal;
struct VertexIn {
  float4 position [[ attribute(0) ]];
};
vertex float4 vertex_main(const VertexIn vertex_in
[[ stage_in ]]) {
  return vertex_in.position;
}
fragment float4 fragment_main() {
  return float4(1, 0, 0, 1);
}
"""

let library = try device.makeLibrary(source: shader, options: nil)
let vertexFunction = library.makeFunction(name: "vertex_main")
let fragmentFunction = library.makeFunction(name:
"fragment_main")

let pipelineDescriptor = MTLRenderPipelineDescriptor()
pipelineDescriptor.colorAttachments[0].pixelFormat = .bgra8Unorm
pipelineDescriptor.vertexFunction = vertexFunction
pipelineDescriptor.fragmentFunction = fragmentFunction

pipelineDescriptor.vertexDescriptor = MTKMetalVertexDescriptorFromModelIO(mesh.vertexDescriptor)

let pipelineState = try device.makeRenderPipelineState(descriptor: pipelineDescriptor)

// 1
guard let commandBuffer = commandQueue.makeCommandBuffer(),
// 2
let renderPassDescriptor = view.currentRenderPassDescriptor,
// 3
let renderEncoder = commandBuffer.makeRenderCommandEncoder(descriptor: renderPassDescriptor)
else { fatalError() }

renderEncoder.setRenderPipelineState(pipelineState)

renderEncoder.setVertexBuffer(mesh.vertexBuffers[0].buffer, offset: 0, index: 0)

guard let submesh = mesh.submeshes.first else {
 fatalError()
}

renderEncoder.drawIndexedPrimitives(type: .triangle,
                          indexCount: submesh.indexCount,
                          indexType: submesh.indexType,
                          indexBuffer: submesh.indexBuffer.buffer, indexBufferOffset: 0)

// 1
renderEncoder.endEncoding()
// 2
guard let drawable = view.currentDrawable else {
  fatalError()
}
// 3
commandBuffer.present(drawable)
commandBuffer.commit()

PlaygroundPage.current.liveView = view
```

![metal code result image](./woosuk.png)  