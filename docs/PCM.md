---
icon: material/music-circle-outline
---


![Local image](./images/PCM.png){: style="display: block; margin: 0 auto"}

<H2 style="text-align: center;">A Brief Overview of Pulse Code Modulation [PCM]</H2>

!!! deep-dive "Communication"

    ### Communication {.toc-hidden-header}
    
    - Communication refers to the transfer of information from one place to another. From dropping a letter to developments like landline phones, mobiles, FAX machines, SMS, MMS, e-mail, video calling are all part of communication.
    
    - When information is transmitted from one place to another, we can expect delays, noise, data loss and much more. Sometimes due to noise or disturbance, it is hard to receive the message as it is transmitted.
    
    - Here comes a concept which is known as modulation, which aids in the proper reception of the transmitted signal.
    
!!! warning "Modulation"

    ### Modulation {.toc-hidden-header}
    
    Modulation is the process of altering one or more properties of a periodic waveform known as a carrier signal with respect to the [modulation](https://byjus.com/physics/modulation-and-demodulation/) signal, which contains information to be transmitted. Modulation is performed by the device known as a modulator, and this technique is mainly used to overcome the interference of the signal. Modulation techniques typically aid in long-distance communication.
    
    !!! warning "Modulation is of two types:"
    
        #### Two Types {.toc-hidden-header}
        
        Analog Modulation
        Digital modulation
        
    In analog modulation, a continuously varying sine wave is considered a carrier wave. This wave modulates the data signal. In amplitude modulation, three parameters can be altered, they are: frequency, amplitude and phase.
    
    !!! warning "Types of analog modulation are:"
    
        #### Anolog Types (3) {.toc-hidden-header}
        
        Amplitude modulation (AM)
        Frequency modulation (FM)
        Phase modulation (PM)
        
        

!!! desc "Digital Modulation"

    ### Digital Modulation {.toc-hidden-header}
    
    - In digital modulation, an analog carrier signal is modulated by a discrete signal. The process of encoding affects the bandwidth of the transmitted signal and its robustness to channel impairments. In digital modulation, a message or information is converted into the amplitude, phase, or [frequency](https://byjus.com/physics/period-angular-frequency/) of the transmitted signal. In the encoding process, the signal is converted from analog to digital form and then the modulated signal is carried by using a carrier wave.
    
    !!! warning "Digital modulation is of the following types:"
    
        #### Three Types {.toc-hidden-header}
        
        Pulse Amplitude modulation (PAM)
        Pulse width modulation (PWM)
        Pulse code modulation (PCM)
        
    
!!! git "Digital Modulation Techniques"

    In this article, let us study in detail about one of the digital modulation techniques, Pulse code modulation (PCM).
    
!!! deep-dive "Pulse Code Modulation"

    ### PCM {.toc-hidden-header}
    
    - When a digital signal undergoes Pulse Code Modulation, it converts the analog information into a binary sequence (1 and 0). Through the demodulation process, we can obtain the original analog signal. The figure below represents the output of the PCM signal with respect to the sine wave.
    
    ![](imgs/20251231-224303.png){: style="display: block; margin: 0 auto"}
    
    - Pulse Code Modulation techniques are used to produce a series of numbers or digits in binary form. Hence this process is called digital modulation. The amplitude at that particular time of the signal sample is indicated by the binary codes.
    
    - In the PCM process, a sequence of coded pulses indicates the message signal. This message signal represents amplitude and time.
    
    !!! warning "Pulse code modulations are of two types:"
    
        Differential pulse code modulation (DPCM)
        Adaptive differential pulse code modulation (ADPCM)
        
    
!!! deep-dive "Differential pulse-code Modulation"

    #### Differential PCM {.toc-hidden-header}
    
    - Differential pulse-code modulation is a signal encoding process which adds functionalities based on the prediction of the samples of the signal.
    
    - Adaptive differential pulse-code modulation is a technique in which the size of the quantization step is varied, to allow the further reduction of the required data bandwidth to a given signal-to-noise ratio.
    
    !!! desc "PCM Process"
    
        - The Pulse Code Modulation process is done through the following steps:
        
            - Sampling
            - Quantisation
            - Coding
        
        ---
        
        Block diagram of the Pulse Code Modulation process is as shown in the figure below.
        
        ![](imgs/20251231-224415.png){: style="display: block; margin: 0 auto"}
        
        - In the PCM process, it is possible to digitise all forms of analog data, including music, telemetry, voice, full-motion video. To obtain a pulse code modulated waveform from an analog waveform at the transmitter end and to convert the message signal into the binary form, a process known as quantisation is used.
        
        - At the receiver end of the pulse code circuit, demodulation takes place, and the signal is converted into pulses with the same quantum levels.
        
        ---
        
        __Low Pass Filter</strong__
        
        - A low pass filter helps in removing the high-frequency components included in the input of the analog signal. These frequency components are higher than the highest frequency of the message signal. Hence, a low pass filter is added in the pulse code modulation technique to avoid aliasing of the message signal.
        
        ---
        
        __Sampler__
        
        - Sampler helps to collect the sample data at any time of the message signal, in order to reform the original signal. As per the sampling theorem, the sampling rate is greater than the highest frequency component of the message signal.
        
        ---
        
        __Quantizer__
        
        -Quantizer helps to minimise the error through the process known as quantizing. The sampled output when passed through a quantizer, reduces the unnecessary bits and also helps in compressing the obtained values.
        
        ---
        
        __Encoder__
        
        - The encoder is used for digitising the analog signal. Encoder helps to allot each quantised level through a binary code. The sample-and-hold process is adopted in this. Low pass filter, sampler, and quantiser aids to convert analog to digital forms. Encoding also aids in minimising the usage of bandwidth.
        
        ---
        
        __Regenerative Repeater__
        
        - Regenerative repeater is used to compensate for the signal loss and also reform the signal. It also helps to increase signal strength. Hence, the output of the channel is equipped with one regenerative repeater circuit.
        
        ---
        
        __Decoder__
        
        - The decoder helps to form the original signal by decoding the pulse coded waveform. Decoder acts as the demodulator.
        
        ----
        
        __Reconstruction Filter__
        
        - The reconstruction filter helps to obtain the original signal. In the pulse code modulator circuit, the given analog signal is digitized, coded and sampled. The resultant signal is transmitted in an analog form. In order to obtain the original signal, the whole process is repeated in a reverse pattern 
        
    
!!! desc "__Advantages and Disadvantages__"

    - __Advantages__
    
        - Pulse Code Modulation is used in long-distance communication.
        - The efficiency of the transmitter in PCM is high.
        - Higher noise immunity is seen.
        - Efficient method.
      
    - __Disadvantages__
    
        - The bandwidth requirement is high.
        - PCM is a complex process, since it involves encoding, decoding and quantisation of the circuit.
        - Applications of Pulse Code Modulation
        - It is used in telephony and compact discs.
        - Pulse Code Modulation is used in satellite transmission systems and space communications.
      
    - Read more about [modulation and the need for modulation](https://byjus.com/physics/modulation-need-modulation).
    

!!! deep-dive "Trivia"
    **Related links:**
    
    ### Trivia {.toc-hidden-header}
    
    * [Relative Motion &rarr;](https://byjus.com/jee/relative-motion/)
    * [Protection against Earthquakes &rarr;](https://byjus.com/physics/protection-against-earthquake/)
    * [Lenz Law &rarr;](https://byjus.com/physics/lenzs-law/)
    * [Radioactivity &rarr; Alpha Decay](https://byjus.com/physics/radioactivity-alpha-decay/)

    ??? decision "Frequently Asked Questions on Pulse Code Modulation"
        
        #### Q&A {.toc-hidden-header}
        
        **Question 1.**
        
        - Why is a decoder used?
            - The decoder helps to decode the pulse coded waveform to reproduce the original signal.

        **Question 2.**

        - What are the types of Pulse code modulations?
            - Differential pulse code modulation (DPCM)
            - Adaptive differential pulse code modulation (ADPCM)

        **Question 3.**

        - Which component helps to increase the signal strength in PCM?
            - Regenerative Repeater.

        **Question 4.**

        - What are the types of digital modulation?
            - Pulse Amplitude modulation (PAM)
            - Pulse width modulation (PWM)
            - Pulse code modulation (PCM)

        **Question 5.**

        - In the PCM process, sequence of coded pulses indicates what?
            - Message signal.

    
<iframe width="560" height="315" src="https://www.youtube.com/embed/wCdgWp9NZlc?si=CvT_YNo5qsN-SRKU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


