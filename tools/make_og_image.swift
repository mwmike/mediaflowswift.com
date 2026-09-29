// Draws images/og-image.png, the picture shown when a page of mediaflowswift.com is shared (Open Graph and
// Twitter cards): 1200 × 630, the site's teal, the favicon's mark in white, the name and what it is.
//
//   swift tools/make_og_image.swift [images/og-image.png]
//
// The mark is favicon.svg's, in its own 28-unit space, drawn the way the app icon's script draws it
// (MediaFlowSwift/scripts/make_app_icon.swift in the app repository) at its larger sizes: a film frame (x 4, y 7,
// 20 × 14, corner 2.5, stroke 1.8); sprocket marks at x 7–10 and 18–21 on rows 11, 14, 17 (stroke 1.5, round
// caps); a play triangle (12.3, 11.6) (16.4, 14) (12.3, 16.4), clear of the sprocket ends. Everything is centred,
// so a platform that crops the card to a square or to 2:1 still shows all of it. The text is the system sans at
// sizes that stay readable when the card is shown small.
import AppKit

let width = 1200, height = 630
let W = CGFloat(width), H = CGFloat(height)

let teal = NSColor(srgbRed: 0x0b / 255, green: 0x6e / 255, blue: 0x78 / 255, alpha: 1)       // --accent
let tealTop = NSColor(srgbRed: 0x12 / 255, green: 0x80 / 255, blue: 0x8b / 255, alpha: 1)
let tealBottom = NSColor(srgbRed: 0x08 / 255, green: 0x5c / 255, blue: 0x65 / 255, alpha: 1)
let soft = NSColor(srgbRed: 0xdc / 255, green: 0xef / 255, blue: 0xef / 255, alpha: 1)       // --accent-soft

let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height, bitsPerSample: 8,
                           samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB,
                           bytesPerRow: 0, bitsPerPixel: 0)!
rep.size = NSSize(width: W, height: H)
NSGraphicsContext.saveGraphicsState()
let context = NSGraphicsContext(bitmapImageRep: rep)!
NSGraphicsContext.current = context
let cg = context.cgContext

// Background: the teal, with the app icon's gentle top-to-bottom light.
let gradient = CGGradient(colorsSpace: CGColorSpace(name: CGColorSpace.sRGB),
                          colors: [tealTop.cgColor, teal.cgColor, tealBottom.cgColor] as CFArray,
                          locations: [0, 0.5, 1])!
cg.drawLinearGradient(gradient, start: CGPoint(x: 0, y: H), end: CGPoint(x: 0, y: 0), options: [])

// The text, measured first so the whole group can be centred.
let titleFont = NSFont.systemFont(ofSize: 104, weight: .bold)
let subtitleFont = NSFont.systemFont(ofSize: 46, weight: .medium)
let title = NSAttributedString(string: "MediaFlowSwift",
                               attributes: [.font: titleFont, .foregroundColor: NSColor.white, .kern: -1.0])
let subtitle = NSAttributedString(string: "Video footage manager for Mac",
                                  attributes: [.font: subtitleFont, .foregroundColor: soft])
let titleSize = title.size(), subtitleSize = subtitle.size()
guard titleSize.width < W - 160, subtitleSize.width < W - 160 else { fatalError("text too wide for the card") }

// The mark: favicon units at s points each. The frame with its stroke spans y 6.1–21.9, about 16 units.
let s: CGFloat = 12
let markHeight = 16 * s
let gapMarkTitle: CGFloat = 40, gapTitleSubtitle: CGFloat = 10
let group = markHeight + gapMarkTitle + titleSize.height + gapTitleSubtitle + subtitleSize.height
let top = (H - group) / 2                       // distance from the top edge to the top of the group

// Draw the mark in the favicon's orientation (y down).
cg.saveGState()
cg.translateBy(x: 0, y: H)
cg.scaleBy(x: 1, y: -1)
let ox = W / 2 - 14 * s                         // favicon x 14 is the centre
let oy = top - 6 * s                            // favicon y 6 is the top of the stroked frame
func p(_ x: CGFloat, _ y: CGFloat) -> CGPoint { CGPoint(x: ox + x * s, y: oy + y * s) }
cg.setStrokeColor(NSColor.white.cgColor)
cg.setFillColor(NSColor.white.cgColor)
let frame = CGRect(origin: p(4, 7), size: CGSize(width: 20 * s, height: 14 * s))
cg.addPath(NSBezierPath(roundedRect: frame, xRadius: 2.5 * s, yRadius: 2.5 * s).cgPath)
cg.setLineWidth(1.8 * s); cg.strokePath()
cg.setLineWidth(1.5 * s); cg.setLineCap(.round)
for row: CGFloat in [11, 14, 17] {
    for (a, b) in [(CGFloat(7), CGFloat(10)), (CGFloat(18), CGFloat(21))] {
        cg.move(to: p(a, row)); cg.addLine(to: p(b, row))
    }
}
cg.strokePath()
cg.move(to: p(12.3, 11.6)); cg.addLine(to: p(16.4, 14)); cg.addLine(to: p(12.3, 16.4))
cg.closePath(); cg.fillPath()
cg.restoreGState()

// The text, in AppKit's own orientation (y up): draw(at:) takes the bottom-left of the line.
let titleTop = top + markHeight + gapMarkTitle
title.draw(at: NSPoint(x: (W - titleSize.width) / 2, y: H - titleTop - titleSize.height))
let subtitleTop = titleTop + titleSize.height + gapTitleSubtitle
subtitle.draw(at: NSPoint(x: (W - subtitleSize.width) / 2, y: H - subtitleTop - subtitleSize.height))

NSGraphicsContext.restoreGraphicsState()

let out = URL(fileURLWithPath: CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "images/og-image.png")
let data = rep.representation(using: .png, properties: [:])!
try data.write(to: out)
print("wrote \(out.path) (\(width) × \(height), \(data.count / 1024) KB)")
