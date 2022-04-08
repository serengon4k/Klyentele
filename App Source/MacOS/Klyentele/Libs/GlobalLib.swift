//
//  GlobalLib.swift
//  Klyentele
//
//  Created by Devin B on 4/6/22.
//

import Foundation
import SwiftUI


//Assets and Global Library

struct NormalButton: ButtonStyle {
    func makeBody(configuration: Self.Configuration) -> some View {
        configuration.label
            .foregroundColor(Color(#colorLiteral(red: 0, green: 0.83, blue: 0.6, alpha: 1)))
            .frame(width: 138, height: 46)
            .font(.custom("Montserrat", size: 24))
            .background(
                RoundedRectangle(cornerRadius: 24)
                    .fill(Color("ButtonBackground"))
                    .frame(width: 138, height: 46))
    }
}

struct ModeSelectionButton: ButtonStyle {
    func makeBody(configuration: Self.Configuration) -> some View {
        configuration.label
            .foregroundColor(Color(#colorLiteral(red: 0, green: 0.83, blue: 0.6, alpha: 1)))
            .frame(width: 200, height: 201)
            .font(.custom("Montserrat", size: 96))
            .background(
                RoundedRectangle(cornerRadius: 24)
                    .fill(Color("ButtonBackground"))
                    .frame(width: 200, height: 201))
    }
}
